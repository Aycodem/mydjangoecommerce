from django.urls import path
from . import views


urlpatterns=[
    path('',views.formcreate,name='create'),
    path('view/',views.view,name='view'),
    path("view/<int:pk>/delete/",views.delete,name='delete'),
    path("view/<int:pk>/update/",views.update,name='update'),
    path('apiview/<int:pk>/',views.showpost_detail,name='showpost'),
    path('apiview',views.ListCreate_ApiView,name='apilist_view'),
    path('apiview/<int:pk>/update',views.Updateview,name='Update'),
    path('apiview/<int:pk>/delete',views.Delete_view,name='delete'),

]