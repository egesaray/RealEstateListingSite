from django.shortcuts import render ,redirect
from django.contrib.auth import  authenticate , login ,logout
from django.http import HttpResponseRedirect
from .decorators import unauthenticated_user
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
from .models import *
from .filters import *
from django.db.models import Q




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


def homepagealternative(request):
    return render(request, 'main/homepagealternative.html')


def homepage(request):
    forsale = 'forsale'
    forrent = 'forrent'

    return render(request, 'main/homepage.html',{'forsale':forsale , 'forrent':forrent})


def list(request,RoS):
    if RoS == 'forsale':
        cu = Post.objects.all().filter(postType='For Sale')
    elif RoS =='forrent':
        cu = Post.objects.all().filter(postType='For Rent')

    myFilter = PostFilter(request.GET , queryset=cu)
    cu = myFilter.qs

    return render(request, 'main/list.html' ,{'cu' :cu , 'myFilter':myFilter} )



def postlistings(request,RoS):
    if RoS == 'forsale':
        cu = Post.objects.all().filter(postType='For Sale')
    elif RoS =='forrent':
        cu = Post.objects.all().filter(postType='For Rent')

    query = request.GET.get('query')
    price_from = request.GET.get('price_from',0)
    price_to = request.GET.get('price_to', 1000000000)
    min_area = request.GET.get('min_area', 0)
    max_area = request.GET.get('max_area', 4000)
    min_age = request.GET.get('min_age', 0)
    max_age = request.GET.get('max_age', 100)


    if query != None:
        print("sadasdas")
        cu = cu.filter(Q(post_title__icontains = query) | Q(location__icontains = query)| Q(area__icontains = query)| Q(building_type__icontains = query))
    else:
        query = ""

    cu = cu.filter(price__gte =price_from).filter(price__lte=price_to)
    cu = cu.filter(area__gte=min_area).filter(area__lte=max_area)
    cu = cu.filter(building_age__gte=min_age).filter(building_age__lte=max_age)

    myFilter = PostFilter(request.GET , queryset=cu)
    cu = myFilter.qs

    context = {
        'cu': cu,
        'RoS': RoS,
        'price_from':price_from,
        'price_to':price_to,
        'min_area':min_area,
        'max_area':max_area,
        'min_age': min_age,
        'max_age': max_age,
        'myFilter': myFilter,
        'query':query,
    }

    return render(request, 'main/postlistings.html' , context )




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
        # imageForm=ImagePost(request.POST,request.FILES)
        images = request.FILES.getlist('images')
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

            for image in images:
                photo = PostImages.objects.create(image =image , gallery=newPost)

            photo.save()

            # area = request.POST['area']  django form kullanılarak çağırılmak istenirse
            # area = request.POST.get('isfurniture')   html ile input kullanularak çağırlmak istenirse

            return redirect('createpost-success')

    return render(request, 'main/createpost.html', context=mydict)


def createpostsuccess(request):
    return render(request, 'main/create-post-success.html')

def productdetails(request, pk):
    posts = Post.objects.get(id=pk)

    pimage = PostImages.objects.filter(gallery=posts)

    return render(request, 'main/product_details.html', { 'posts':posts ,'pimage':pimage} )



def listaddedposts(request):
    user = ourUser.objects.get(user_id=request.user.id)
    posts = Post.objects.all().filter(ouruser=user)
    current_user = request.user
    print("Here--->",current_user.id)
    return render(request, 'main/listaddedposts.html', { 'posts':posts , 'user':user})