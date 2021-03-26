from django.urls import path
from .import views

urlpatterns = [
    # leave as empty string fo base url
    path('', views.homepage, name="homepage"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('list/<str:RoS>', views.list, name="list"),
    path('createpost/', views.createpost, name="createpost"),
    ]