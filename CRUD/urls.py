from django.urls import path
from . import views


urlpatterns=[
    path('',views.create,name='create'),
    path('view/',views.view,name='view'),
    # path('view/<int:pk>/',views.showpost,name='showpost'),
    path("view/<int:pk>/delete/",views.delete,name='delete'),
    path("view/<int:pk>/update/",views.update,name='update')

]