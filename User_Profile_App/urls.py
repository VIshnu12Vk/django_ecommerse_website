from django.contrib import admin
from django.urls import path
from User_Profile_App import views
urlpatterns = [
    path('login/',views.loginaccount,name='login'),
    path('logout/',views.logoutaccount,name="logout"),
    path('signup/',views.signupaccount,name="signup"),
    path('user_account/',views.account_user,name="user_account"),
]