
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login,  name = 'login' ),
    path('logout/', views.logout,  name = 'logout' ),
    path('register/', views.register,  name = 'register' ),
    path('dashboard/', views.dashboard , name = 'dashboard'),
    path('dashboard/<int:pk>/', views.delete_idea , name = 'delete_idea'),
    path('dashboard/edit/<int:pk>/', views.edit_idea , name = 'edit_idea'),
    path('forgotpassword/', views.forgot_password , name = 'forgotpassword'),
    path('change_password/', views.changepassword,  name = 'changepassword' ),
    # path('dashboard/account_info', views.account_info , name = 'account_info'),



   
]
