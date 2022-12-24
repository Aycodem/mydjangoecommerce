from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns =[
    path('',views.Showall,name='product-list'),
    path('create/',views.CreateProduct ,name='create_product'),
    path('<int:pk>/',views.Viewproduct,name='view_product'),
    path('<int:pk>/update/',views.UpdateProduct,name='update_product'),
    path('<int:pk>/delete/',views.DeleteProduct,name='delete_product'),
]