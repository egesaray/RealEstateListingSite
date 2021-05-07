from django.urls import path
from . import views

urlpatterns = [
    # leave as empty string fo base url
    path('', views.homepage, name="homepage"),
    path('homepagealternative/', views.homepagealternative),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('list/<str:RoS>', views.list, name="list"),
    path('createpost/', views.createpost, name="createpost"),
    path('createpost-success/', views.createpostsuccess, name="createpost-success"),
    path('product_details/<int:pk>', views.productdetails, name="product_details"),
    path('postlistings/<str:RoS>', views.postlistings, name="postlistings"),
    path('listaddedposts/', views.listaddedposts, name="listaddedposts"),
    path('editpost/<int:pk>', views.editpost, name="editpost"),
    path('delete-post/<int:pk>', views.deletepost, name='delete-post'),
    path('delete-photo/<int:pk>', views.deletephoto, name='delete-photo'),
    path('adminPage/', views.adminPage, name="adminPage"),
    path('user/', views.user, name="user"),
    path('sale/', views.sale, name="sale"),
    path('rent/', views.rent, name="rent"),
    path('user-delete/<int:pk>', views.delete_user, name="deleteuser"),
    path('post_delete/<int:pk>', views.delete_post, name="deletepost"),
    path('graphs/', views.graphs, name="graphs"),
    path('editpost_admin/<int:pk>', views.editpost_admin, name="editpost_admin"),
    path('user_detail/<int:pk>', views.user_detail, name="user_detail"),

]
