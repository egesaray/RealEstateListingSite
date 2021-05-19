from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # leave as empty string fo base url
    path('', views.homepage, name="homepage"),
    path('homepagealternative/', views.homepagealternative, name="homepagealternative"),
    path('loginpage/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('list/<str:RoS>', views.list, name="list"),
    path('createpost/', views.createpost, name="createpost"),
    path('createpost-success/', views.createpostsuccess, name="createpost-success"),
    path('product_details/<int:pk>', views.productdetails, name="product_details"),
    path('productbyloc/<str:loc>', views.productbyloc, name="product_loc"),#search on  map
    path('postlistings/<str:RoS>', views.postlistings, name="postlistings"),
    path('listaddedposts/', views.listaddedposts, name="listaddedposts"),
    path('editpost/<int:pk>', views.editpost, name="editpost"),
    path('editprofile/', views.editprofile, name="editprofile"),
    path('delete-post/<int:pk>', views.deletepost, name='delete-post'),
    path('delete-photo/<int:pk>', views.deletephoto, name='delete-photo'),
    path('adminpage/', views.adminpage, name="adminpage"),
    path('user/', views.user, name="user"),
    path('sale/', views.sale, name="sale"),
    path('rent/', views.rent, name="rent"),
    path('user-delete/<int:pk>', views.delete_user, name="deleteuser"),
    path('post_delete/<int:pk>', views.delete_post, name="deletepost"),
    path('graphs/', views.graphs, name="graphs"),
    path('editpost_admin/<int:pk>', views.editpost_admin, name="editpost_admin"),
    path('user_detail/<int:pk>', views.user_detail, name="user_detail"),
    path('post_detail/<int:pk>', views.post_detail, name="post_detail"),
path( 'changepassword', views.changepassword, name="changepassword"),

    #password set
     path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="main/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"),
        name="password_reset_complete"),


]
