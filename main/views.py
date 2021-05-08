from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .decorators import unauthenticated_user, allowed_users
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
from .models import *
from .filters import *
from django.db.models import Q
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


def logoutUser(request):
    logout(request)
    return redirect('homepage')


@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('adminPage')
            else:
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
            usergroup = Group.objects.get(name='customer')
            user.groups.add(usergroup)

            return redirect('loginpage')

    context = {'form': form}
    return render(request, 'main/register.html', context)


def homepagealternative(request):
    return render(request, 'main/homepagealternative.html')


@login_required
@allowed_users(allowed_roles=['admin'])
def adminPage(request):
    sales = Post.objects.all().filter(postType='For Sale')
    sales_count = sales.count()

    rents = Post.objects.all().filter(postType='For Rent')
    rents_count = rents.count()

    users = ourUser.objects.all()
    users_count = users.count()

    context = {

        'sales_count': sales_count,
        'rents_count': rents_count,
        'users_count': users_count,
    }
    return render(request, 'main/adminpage.html', context)


@login_required
@allowed_users(allowed_roles=['admin'])
def user(request):
    sales = Post.objects.all().filter(postType='For Sale')
    sales_count = sales.count()

    rents = Post.objects.all().filter(postType='For Rent')
    rents_count = rents.count()

    users = ourUser.objects.all()
    users_count = users.count()

    context = {

        'users': users,
        'rents': rents,
        'sales': sales,
        'sales_count': sales_count,
        'rents_count': rents_count,
        'users_count': users_count,
    }

    return render(request, 'main/user.html', context)


@login_required
@allowed_users(allowed_roles=['admin'])
def sale(request):
    sales = Post.objects.all().filter(postType='For Sale')
    sales_count = sales.count()

    rents = Post.objects.all().filter(postType='For Rent')
    rents_count = rents.count()

    users = ourUser.objects.all()
    users_count = users.count()

    context = {
        'users': users,
        'rents': rents,
        'sales': sales,
        'sales_count': sales_count,
        'rents_count': rents_count,
        'users_count': users_count,
    }
    return render(request, 'main/sale.html', context)


@login_required
@allowed_users(allowed_roles=['admin'])
def rent(request):
    sales = Post.objects.all().filter(postType='For Sale')
    sales_count = sales.count()

    rents = Post.objects.all().filter(postType='For Rent')
    rents_count = rents.count()

    users = ourUser.objects.all()
    users_count = users.count()

    context = {
        'users': users,
        'rents': rents,
        'sales': sales,
        'sales_count': sales_count,
        'rents_count': rents_count,
        'users_count': users_count,
    }
    return render(request, 'main/rent.html', context)


@login_required
@allowed_users(allowed_roles=['admin'])
def graphs(request):
    sales = Post.objects.all().filter(postType='For Sale')
    sales_count = sales.count()

    rents = Post.objects.all().filter(postType='For Rent')
    rents_count = rents.count()

    users = ourUser.objects.all()
    users_count = users.count()

    context = {

        'users': users,
        'rents': rents,
        'sales': sales,
        'sales_count': sales_count,
        'rents_count': rents_count,
        'users_count': users_count,
    }

    return render(request, 'main/graphs.html', context)


def homepage(request):
    forsale = 'forsale'
    forrent = 'forrent'

    return render(request, 'main/homepage.html', {'forsale': forsale, 'forrent': forrent})


def list(request, RoS):
    if RoS == 'forsale':
        cu = Post.objects.all().filter(postType='For Sale')
    elif RoS == 'forrent':
        cu = Post.objects.all().filter(postType='For Rent')

    myFilter = PostFilter(request.GET, queryset=cu)
    cu = myFilter.qs

    return render(request, 'main/list.html', {'cu': cu, 'myFilter': myFilter})


def postlistings(request, RoS):
    if RoS == 'forsale':
        cu = Post.objects.all().filter(postType='For Sale')
    elif RoS == 'forrent':
        cu = Post.objects.all().filter(postType='For Rent')

    query = request.GET.get('query')
    price_from = request.GET.get('price_from', 0)
    price_to = request.GET.get('price_to', 1000000000)
    min_area = request.GET.get('min_area', 0)
    max_area = request.GET.get('max_area', 4000)
    min_age = request.GET.get('min_age', 0)
    max_age = request.GET.get('max_age', 100)
    min_room_num = request.GET.get('min_room_num', 0)
    max_room_num = request.GET.get('max_room_num', 20)
    min_floor_num = request.GET.get('min_floor_num', 0)
    max_floor_num = request.GET.get('max_floor_num', 100)

    if query != None:
        print("sadasdas")
        cu = cu.filter(Q(post_title__icontains=query) | Q(location__icontains=query) | Q(area__icontains=query) | Q(
            building_type__icontains=query))
    else:
        query = ""

    cu = cu.filter(price__gte=price_from).filter(price__lte=price_to)
    cu = cu.filter(area__gte=min_area).filter(area__lte=max_area)
    cu = cu.filter(building_age__gte=min_age).filter(building_age__lte=max_age)
    cu = cu.filter(room__gte=min_room_num).filter(room__lte=max_room_num)
    cu = cu.filter(floor__gte=min_floor_num).filter(floor__lte=max_floor_num)

    myFilter = PostFilter(request.GET, queryset=cu)
    cu = myFilter.qs

    context = {
        'cu': cu,
        'RoS': RoS,
        'price_from': price_from,
        'price_to': price_to,
        'min_area': min_area,
        'max_area': max_area,
        'min_age': min_age,
        'max_age': max_age,
        'min_room_num': min_room_num,
        'max_room_num': max_room_num,
        'min_floor_num': min_floor_num,
        'max_floor_num': max_floor_num,
        'myFilter': myFilter,
        'query': query,
    }

    return render(request, 'main/postlistings.html', context)


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
@allowed_users(allowed_roles=['customer'])
def createpost(request):
    postForm = CreatePost()
    imageForm = ImagePost()
    ouruser = request.user.ouruser
    mydict = {'form': postForm, 'imageForm': imageForm}
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
            room = request.POST['room']
            post_description = request.POST['post_description']
            area = request.POST['area']
            isFurniture = request.POST['isFurniture']
            newPost = Post(postType=postType, building_type=building_type, location=location, post_title=post_title,
                           price=price, building_age=building_age, floor=floor, room=room,
                           post_description=post_description, area=area, isFurniture=isFurniture, ouruser=ouruser)
            newPost.save()

            for image in images:
                photo = PostImages.objects.create(image=image, gallery=newPost)

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

    return render(request, 'main/product_details.html', {'posts': posts, 'pimage': pimage})


@login_required
@allowed_users(allowed_roles=['customer'])
def listaddedposts(request):
    fuser = ourUser.objects.get(user_id=request.user.id)
    posts = Post.objects.all().filter(ouruser=fuser)
    mydict = {'posts': posts, 'fuser': fuser}
    return render(request, 'main/listaddedposts.html', context=mydict)


@login_required
@allowed_users(allowed_roles=['customer'])
def editpost(request, pk):
    fuser = Post.objects.get(id=pk)
    p_form = CreatePost(instance=fuser)
    pimage = PostImages.objects.filter(gallery=fuser)
    mydict = {'fuser': fuser, 'p_form': p_form, 'pimage': pimage}
    if request.method == 'POST':
        p_form = CreatePost(request.POST, instance=fuser)
        images = request.FILES.getlist('images')
        if p_form.is_valid():
            post = p_form.save()
            fuser.save()

            if images != None:
                for image in images:
                    photo = PostImages.objects.create(image=image, gallery=fuser)
                    photo.save()
                return redirect('listaddedposts')

    return render(request, 'main/editpost.html', context=mydict)


def deletepost(request, pk):
    if request.method == 'POST':
        fuser = Post.objects.get(id=pk)
        pimage = PostImages.objects.filter(gallery=fuser)
        fuser.delete()
        pimage.delete()
    return redirect('listaddedposts')


def deletephoto(request, pk):
    pimage = PostImages.objects.filter(id=pk)
    pimage.delete()

    return redirect(request.META['HTTP_REFERER'])


@login_required
@allowed_users(allowed_roles=['admin'])
def delete_user(request, pk):
    user = ourUser.objects.get(id=pk)
    sales = Post.objects.all().filter(postType='For Sale')
    sales_count = sales.count()

    rents = Post.objects.all().filter(postType='For Rent')
    rents_count = rents.count()

    users = ourUser.objects.all()
    users_count = users.count()
    if request.method == 'POST':
        user.delete()
        return redirect('user')
    context = {
        'user': user,
        'sales_count': sales_count,
        'rents_count': rents_count,
        'users_count': users_count,
    }
    return render(request, 'main/user-delete.html', context)


@login_required
@allowed_users(allowed_roles=['admin'])
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    sales = Post.objects.all().filter(postType='For Sale')
    sales_count = sales.count()

    rents = Post.objects.all().filter(postType='For Rent')
    rents_count = rents.count()

    users = ourUser.objects.all()
    users_count = users.count()
    if request.method == 'POST':
        post.delete()
        if post.postType == 'For Sale':
            return redirect('sale')
        else:
            return redirect('rent')

    context = {
        'post': post,
        'sales_count': sales_count,
        'rents_count': rents_count,
        'users_count': users_count,
    }
    return render(request, 'main/post_delete.html', context)


@login_required
@allowed_users(allowed_roles=['admin'])
def editpost_admin(request, pk):
    fuser = Post.objects.get(id=pk)
    p_form = CreatePost(instance=fuser)
    pimage = PostImages.objects.filter(gallery=fuser)

    sales = Post.objects.all().filter(postType='For Sale')
    sales_count = sales.count()

    rents = Post.objects.all().filter(postType='For Rent')
    rents_count = rents.count()

    users = ourUser.objects.all()
    users_count = users.count()
    mydict = {'fuser': fuser, 'p_form': p_form, 'pimage': pimage, 'sales_count':sales_count,'rents_count':rents_count,'users_count':users_count}
    if request.method == 'POST':
        p_form = CreatePost(request.POST, instance=fuser)
        images = request.FILES.getlist('images')
        if p_form.is_valid():
            post = p_form.save()
            post_name = p_form.cleaned_data.get('post_title')
            messages.success(request, f'{post_name} has been added')
            fuser.save()

            if images != None:
                for image in images:
                    photo = PostImages.objects.create(image=image, gallery=fuser)
                    photo.save()
                if fuser.postType=='For Sale':
                    return redirect('sale')
                else:
                    return redirect('rent')

    return render(request, 'main/editpost_admin.html', context=mydict)


@login_required
@allowed_users(allowed_roles=['admin'])
def user_detail(request, pk):


    sales = Post.objects.all().filter(postType='For Sale')
    sales_count = sales.count()

    rents = Post.objects.all().filter(postType='For Rent')
    rents_count = rents.count()

    users = ourUser.objects.all()
    users_count = users.count()

    user = ourUser.objects.get(id=pk)

    context = {
        'user': user,
        'sales_count': sales_count,
        'rents_count': rents_count,
        'users_count': users_count,

    }
    return render(request, 'main/user_detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def post_detail(request, pk):


    sales = Post.objects.all().filter(postType='For Sale')
    sales_count = sales.count()

    rents = Post.objects.all().filter(postType='For Rent')
    rents_count = rents.count()

    users = ourUser.objects.all()
    users_count = users.count()

    post = Post.objects.get(id=pk)

    context = {
        'post': post,
        'sales_count': sales_count,
        'rents_count': rents_count,
        'users_count': users_count,

    }
    return render(request, 'main/post_detail.html', context)


def productbyloc(request, loc):
    location=loc
    posts = Post.objects.all()
    posts = posts.filter(Q(location__icontains=loc))
    mydict = {'posts': posts,'location':location}
    return render(request, 'main/productByLocation.html', context=mydict)



