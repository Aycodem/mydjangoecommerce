from django.http import HttpResponse
from django.shortcuts import redirect

#this is used is to control authentication and permission 

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):

        if request.user.is_authenticated:
            return redirect('crud/view')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func