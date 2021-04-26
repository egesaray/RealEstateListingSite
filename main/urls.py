from django.urls import path
from .import views

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
    path('postlistings/<str:RoS>',views.postlistings, name="postlistings" ),
    path('listaddedposts/',views.listaddedposts, name="listaddedposts" ),
    path('editpost/<int:pk>',views.editpost, name="editpost" ),
     path('update-success/', views.updatesuccess, name="update-success"),
    ]
