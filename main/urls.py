from django.urls import path
from .import views

urlpatterns = [
    # leave as empty string fo base url
    path('', views.homepage, name="homepage"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('list/', views.list, name="list"),
    path('createpost/', views.createpost, name="createpost"),
    ]