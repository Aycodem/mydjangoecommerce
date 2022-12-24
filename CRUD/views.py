from django.shortcuts import render,redirect
from .models import Post
from .serializer import PostSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib import messages
from rest_framework import generics

from django.contrib.auth.decorators import login_required
from .forms import PostForm
# Create your views here.

# @api_view(['GET'])

"""first way to create form"""
def create(request):
    if request.method == "POST":
         name=request.POST['name']
         description=request.POST['description']

         if name!='' and description !='':
            post=Post()
            post.name=name
            post.description=description

            post.save()
            messages.info(request,'posted')
            return redirect('view')

    else:
        return render(request,'create.html')



"""The two ways to create a valid form"""



"""second way to create a form"""
def formcreate(request):
    form=PostForm()
    if request.method == "POST":
        form=PostForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('view')
    else:
        return render(request,'create.html')





def update(request,pk):
    post=Post.objects.get(id=pk)
    serializer=PostSerializer(instance=post,data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return redirect('view')

    serializers=PostSerializer(post,many=False)
    return render(request,'update.html', {'show_edit':serializers.data})



def delete(request,pk):
    post=Post.objects.get(id=pk)
    post.delete()
    return redirect('view')



# @login_required(login_url='login')
def view(request):
    posts=Post.objects.all()
    serializer=PostSerializer(posts,many=True)
    return render(request,'view.html',{"posts":serializer.data})

@api_view(['GET'])
def showpost(request,pk):
    post=Post.objects.get(id=pk)
    serializer=PostSerializer(post,many=False,).data
    return Response(serializer)





























#this is class method views







class ShowPostDetailApiView(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

showpost_detail=ShowPostDetailApiView.as_view()


class ListCreateApiView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

ListCreate_ApiView=ListCreateApiView.as_view()


class UpdateApiView(generics.UpdateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    lookup_field='pk'

Updateview=UpdateApiView.as_view()
    



class Deleteview(generics.DestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    lookup_field='pk'
    
    def perform_destroy(self,instance):
        super().perform_destroy(instance)
        

Delete_view=Deleteview.as_view()
   