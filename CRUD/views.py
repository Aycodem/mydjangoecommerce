from django.shortcuts import render,redirect
from .models import Post
from .serializer import PostSerializer
from rest_framework.decorators import api_view

from rest_framework.response import Response
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

# @api_view(['GET'])
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

@login_required(login_url='login')
def view(request):
    posts=Post.objects.all()
    serializer=PostSerializer(posts,many=True)
    return render(request,'view.html',{"posts":serializer.data})

# @api_view(['GET'])
# def showpost(request,pk):
#     post=Post.objects.get(id=pk)
#     serializer=PostSerializer(post,many=False)
#     print(serializer.data)

#     return Response(serializer.data)