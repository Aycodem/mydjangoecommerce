from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns=[
    path('login',views.login ,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('reset_password',auth_view.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent',auth_view.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete',auth_view.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]