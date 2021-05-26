from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
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
from django.contrib.auth.forms import PasswordChangeForm


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
                return redirect('adminpage')
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

            return redirect('login')

    context = {'form': form}
    return render(request, 'main/register.html', context)

def homepage(request):
    forsale = 'forsale'
    forrent = 'forrent'
    adana = Post.objects.all().filter(location='Adana').count()
    istanbulasya = Post.objects.all().filter(location='İstanbulAsya').count()
    istanbulavrupa = Post.objects.all().filter(location='İstanbulAvrupa').count()
    adiyaman = Post.objects.all().filter(location='Adıyaman').count()
    afyonkarahisar = Post.objects.all().filter(location='Afyonkarahisar').count()
    agri = Post.objects.all().filter(location='Ağrı').count()
    amasya = Post.objects.all().filter(location='Amasya').count()
    ankara = Post.objects.all().filter(location='Ankara').count()
    antalya = Post.objects.all().filter(location='Antalya').count()
    artvin = Post.objects.all().filter(location='Artvin').count()
    aydin = Post.objects.all().filter(location='Aydın').count()
    balikesir = Post.objects.all().filter(location='Balıkesir').count()
    bilecik = Post.objects.all().filter(location='Bilecik').count()
    bingol = Post.objects.all().filter(location='Bingöl').count()
    bitlis = Post.objects.all().filter(location='Bitlis').count()
    bolu = Post.objects.all().filter(location='Bolu').count()
    burdur = Post.objects.all().filter(location='Burdur').count()
    bursa = Post.objects.all().filter(location='Bursa').count()
    canakkale = Post.objects.all().filter(location='Çanakkale').count()
    cankiri = Post.objects.all().filter(location='Çankırı').count()
    corum = Post.objects.all().filter(location='Çorum').count()
    denizli = Post.objects.all().filter(location='Denizli').count()
    diyarbakir = Post.objects.all().filter(location='Diyarbakır').count()
    edirne = Post.objects.all().filter(location='Edirne').count()
    elazig = Post.objects.all().filter(location='Elazığ').count()
    erzincan = Post.objects.all().filter(location='Erzincan').count()
    erzurum = Post.objects.all().filter(location='Erzurum').count()
    eskisehir = Post.objects.all().filter(location='Eskişehir').count()
    gaziantep = Post.objects.all().filter(location='Gaziantep').count()
    giresun = Post.objects.all().filter(location='Giresun').count()
    gumushane = Post.objects.all().filter(location='Gümüşhane').count()
    hakkari = Post.objects.all().filter(location='Hakkari').count()
    hatay = Post.objects.all().filter(location='Hatay').count()
    isparta = Post.objects.all().filter(location='Isparta').count()
    mersin = Post.objects.all().filter(location='Mersin').count()
    izmir = Post.objects.all().filter(location='İzmir').count()
    kars = Post.objects.all().filter(location='Kars').count()
    kastamonu = Post.objects.all().filter(location='Kastamonu').count()
    kayseri = Post.objects.all().filter(location='Kayseri').count()
    kirklareli = Post.objects.all().filter(location='Kırklareli').count()
    kirsehir = Post.objects.all().filter(location='Kırşehir').count()
    kocaeli = Post.objects.all().filter(location='Kocaeli').count()
    konya = Post.objects.all().filter(location='Konya').count()
    kutahya = Post.objects.all().filter(location='Kütahya').count()
    malatya = Post.objects.all().filter(location='Malatya').count()
    manisa = Post.objects.all().filter(location='Manisa').count()
    kahramanmaras = Post.objects.all().filter(location='Kahramanmaraş').count()
    mardin = Post.objects.all().filter(location='Mardin').count()
    mugla = Post.objects.all().filter(location='Muğla').count()
    mus = Post.objects.all().filter(location='Muş').count()
    nevsehir = Post.objects.all().filter(location='Nevşehir').count()
    nigde = Post.objects.all().filter(location='Niğde').count()
    ordu = Post.objects.all().filter(location='Ordu').count()
    rize = Post.objects.all().filter(location='Rize').count()
    sakarya = Post.objects.all().filter(location='Sakarya').count()
    samsun = Post.objects.all().filter(location='Samsun').count()
    siirt = Post.objects.all().filter(location='Siirt').count()
    sinop = Post.objects.all().filter(location='Sinop').count()
    sivas = Post.objects.all().filter(location='Sivas').count()
    tekirdag = Post.objects.all().filter(location='Tekirdağ').count()
    tokat = Post.objects.all().filter(location='Tokat').count()
    trabzon = Post.objects.all().filter(location='Trabzon').count()
    tunceli = Post.objects.all().filter(location='Tunceli').count()
    sanliurfa = Post.objects.all().filter(location='Şanlıurfa').count()
    usak = Post.objects.all().filter(location='Uşak').count()
    van = Post.objects.all().filter(location='Van').count()
    yozgat = Post.objects.all().filter(location='Yozgat').count()
    zonguldak = Post.objects.all().filter(location='Zonguldak').count()
    aksaray = Post.objects.all().filter(location='Aksaray').count()
    bayburt = Post.objects.all().filter(location='Bayburt').count()
    karaman = Post.objects.all().filter(location='Karaman').count()
    kirikkale = Post.objects.all().filter(location='Kırıkkale').count()
    batman = Post.objects.all().filter(location='Batman').count()
    sirnak = Post.objects.all().filter(location='Şırnak').count()
    bartin = Post.objects.all().filter(location='Bartın').count()
    ardahan = Post.objects.all().filter(location='Ardahan').count()
    igdir = Post.objects.all().filter(location='Iğdır').count()
    yalova = Post.objects.all().filter(location='Yalova').count()
    karabuk = Post.objects.all().filter(location='Karabük').count()
    kilis = Post.objects.all().filter(location='Kilis').count()
    osmaniye = Post.objects.all().filter(location='Osmaniye').count()
    duzce = Post.objects.all().filter(location='Düzce').count()
    kuzeykibris = Post.objects.all().filter(location='KuzeyKıbrıs').count()


    mydict = {

    'istanbulasya': istanbulasya,
    'istanbulavrupa': istanbulavrupa,
    'adana': adana,
    'adiyaman': adiyaman ,
    'afyonkarahisar': afyonkarahisar ,
    'agri':agri ,
    'amasya': amasya ,
    'ankara': ankara ,
    'antalya': antalya ,
    'artvin': artvin ,
    'aydin': aydin ,
    'balikesir': balikesir ,
    'bilecik': bilecik ,
    'bingol': bingol ,
    'bitlis': bitlis ,
    'bolu': bolu ,
    'burdur': burdur ,
    'bursa': bursa ,
    'canakkale': canakkale ,
    'cankiri': cankiri ,
    'corum': corum ,
    'denizli': denizli ,
    'diyarbakir': diyarbakir ,
    'edirne': edirne ,
    'elazig': elazig ,
    'erzincan': erzincan ,
    'erzurum': erzurum ,
    'eskisehir': eskisehir ,
    'gaziantep': gaziantep ,
    'giresun': giresun,
    'gumushane': gumushane ,
    'hakkari': hakkari ,
    'hatay': hatay ,
    'isparta': isparta ,
    'mersin': mersin ,
    'izmir': izmir ,
    'kars': kars ,
    'kastamonu': kastamonu ,
    'kayseri': kayseri ,
    'kirklareli': kirklareli ,
    'kirsehir': kirsehir ,
    'kocaeli': kocaeli ,
    'konya': konya,
    'kutahya': kutahya ,
    'malatya': malatya ,
    'manisa': manisa ,
    'kahramanmaras': kahramanmaras,
    'mardin': mardin,
    'mugla': mugla,
    'mus': mus,
    'nevsehir': nevsehir,
    'nigde': nigde,
    'ordu': ordu,
    'rize': rize,
    'sakarya': sakarya,
    'samsun': samsun,
    'siirt': siirt,
    'sinop': sinop,
    'sivas': sivas,
    'tekirdag': tekirdag,
    'tokat': tokat,
    'trabzon': trabzon,
    'tunceli': tunceli,
    'sanliurfa': sanliurfa,
    'usak': usak,
    'van': van,
    'yozgat': yozgat,
    'zonguldak': zonguldak,
    'aksaray': aksaray,
    'bayburt': bayburt,
    'karaman': karaman,
    'kirikkale': kirikkale,
    'batman':batman,
    'sirnak': sirnak,
    'bartin': bartin,
    'ardahan': ardahan,
    'igdir': igdir,
    'yalova': yalova,
    'karabuk': karabuk,
    'kilis': kilis,
    'osmaniye': osmaniye,
    'duzce': duzce,
    'kuzeykibris': kuzeykibris,
    'forsale': forsale,
    'forrent': forrent,

              }

    return render(request, 'main/homepage.html', context=mydict)

def homepagealternative(request):
    return render(request, 'main/homepagealternative.html')


@login_required
@allowed_users(allowed_roles=['admin'])
def adminpage(request):

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
    dusername = user.username
    duser = User.objects.get(username=dusername)
    
    queryuser = ourUser.objects.filter(id=pk)
    sales = Post.objects.all().filter(postType='For Sale')
    sales_count = sales.count()

    rents = Post.objects.all().filter(postType='For Rent')
    rents_count = rents.count()

    users = ourUser.objects.all()
    users_count = users.count()
    if request.method == 'POST':

        if len(queryuser) == 0 :
            messages.error(request, ' Error: User is not deleted ')

        uposts = Post.objects.filter(ouruser=user)
        uposts.delete()
        user.delete()
        duser.delete()
        messages.success(request, ' User Successfully Deleted  ')
        return redirect('user')
    context = {
        'users': users,
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
    querypost = Post.objects.filter(id=pk)
    sales = Post.objects.all().filter(postType='For Sale')
    sales_count = sales.count()

    rents = Post.objects.all().filter(postType='For Rent')
    rents_count = rents.count()

    users = ourUser.objects.all()
    users_count = users.count()
    if request.method == 'POST':

        if len(querypost) == 0 :
            messages.error(request, ' Error: Post is not deleted ')

        post.delete()
        messages.success(request,' Post Successfully Deleted  ')
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
            messages.success(request, f'{post_name} has been updated')
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
        'users' : users,
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
        'users': users,
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



@login_required
@allowed_users(allowed_roles=['customer'])
def editprofile(request):
    fuser = ourUser.objects.get(user_id=request.user.id)
    ouser=User.objects.get(id=fuser.user_id)
    userForm=UserForm(instance=ouser)

    p_form = OurUserForm(instance=fuser)

    mydict = {'fuser': fuser, 'p_form': p_form,'userForm':userForm}
    if request.method == 'POST':
        userForm=UserForm(request.POST,instance=ouser)
        p_form = OurUserForm(request.POST, instance=fuser)
        if userForm.is_valid() and p_form.is_valid():
            ouser=userForm.save()
            ouser.save()
            post = p_form.save()
            fuser.username = ouser.username
            fuser.save()


    return render(request, 'main/editprofile.html', context=mydict)

@login_required
@allowed_users(allowed_roles=['customer'])
def changepassword(request):

    form = PasswordChangeForm(data=request.POST, user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # değiştirdikten sonra hala giriş yapmış şekilde kalması için
            return redirect('/')

    return render(request, 'main/changepassword.html', {'form':form})
