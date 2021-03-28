from django.shortcuts import render ,redirect
from django.contrib.auth import  authenticate , login ,logout
from django.http import HttpResponseRedirect
from .decorators import unauthenticated_user
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
from .models import *


def logoutUser(request):
	logout(request)
	return redirect('homepage')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login( request,user)
            return redirect('homepage')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'main/loginpage.html')

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)

            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            ouser = ourUser(username=username, first_name=first_name, last_name=last_name, email=email, user=user)
            ouser.save()
            return redirect('loginpage')

    context = {'form': form}
    return render(request, 'main/register.html' , context)



def homepage(request):
    forsale = 'forsale'
    forrent = 'forrent'

    return render(request, 'main/homepage.html',{'forsale':forsale , 'forrent':forrent})


def list(request,RoS):
    if RoS == 'forsale':
        cu = Post.objects.all().filter(postType='For Sale')
    elif RoS =='forrent':
        cu = Post.objects.all().filter(postType='For Rent')



    return render(request, 'main/list.html' ,{'cu' :cu} )

"""
@login_required
def createpost(request):
    form = CreatePost()
    if request.method=='POST':
        form = CreatePost(request.POST,request.FILES)
        if form.is_valid():
            post=form.save()
            post.save()

    context = {'form': form}

    return render(request, 'main/createpost.html', context)

"""
@login_required
def createpost(request):
    postForm = CreatePost()
    imageForm=ImagePost()
    ouruser = request.user.ouruser
    mydict = {'form': postForm,'imageForm':imageForm}
    if request.method == 'POST':
        postForm = CreatePost(request.POST)
        imageForm=ImagePost(request.POST,request.FILES)
        if postForm.is_valid():
            postType = request.POST['postType']
            building_type = request.POST['building_type']
            location = request.POST['location']
            post_title = request.POST['post_title']
            price = request.POST['price']
            building_age = request.POST['building_age']
            floor = request.POST['floor']
            post_description = request.POST['post_description']
            area = request.POST['area']
            isFurniture=request.POST['isFurniture']
            newPost = Post(postType=postType,building_type=building_type,location=location,post_title=post_title,price=price,building_age=building_age, floor=floor,post_description=post_description,area=area,isFurniture=isFurniture, ouruser=ouruser)
            newPost.save()
            images = imageForm.save()


            # area = request.POST['area']  django form kullanılarak çağırılmak istenirse
            # area = request.POST.get('isfurniture')   html ile input kullanularak çağırlmak istenirse

            return redirect('createpost-success')

    return render(request, 'main/createpost.html', context=mydict)


def createpostsuccess(request):
    return render(request, 'main/create-post-success.html')
