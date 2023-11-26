from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login

from home.forms import ContactForm, SearchForm, LoginForm, SignUpForm
from home.models import Setting, ContactFormMessage, UserProfileForm, UserProfile
from product.models import Product, Category, Images, Comment, CommentForm
from order.models import ShopCart

# Create your views here.
def index(request):
    slider = Product.objects.all() #! Sidebar.html slider içerisinde.
    urunler = Product.objects.order_by('?')[:8] #! .objects.all()[:8] tane resim seç demek! .objects.order_by('?')[:8] ise random şekilde ayarlar.
    context = {'page': 'home',
               'slider': slider,
               'urunler': urunler}
    return render(request, 'index.html', context)

def hakkimizda(request):
    context = {'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    context = {'page': 'referanslar'}
    return render(request, 'referanslar.html', context)

def shop(request):
    context = {'page': 'shop'}
    return render(request, 'shop.html', context)

def detail(request):
    context = {'page': 'detail'}
    return render(request, 'detail.html', context)

def iletisim(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save() #? SAVE DATA
            messages.success(request, "Your message has been sent. Thank you for your message.") #? Kullanıcıya mesajının iletildiğine dair bilgi veriliyor.
            return HttpResponseRedirect('/iletisim') #?Kullanıcıyı iletisim sayfasına gönderir.
        else:
            messages.warning(request, "Your message has'nt been sent.NOT VALID !!")    
    setting = Setting.objects.get(pk=1)
    form = ContactForm
    context = {'page': 'iletisim',
               'form': form}
    return render(request, 'iletisim.html', context)

def categoryProducts(request, id, slug):
    urunKategori = Category.objects.get(pk=id)
    urunler = list(Product.objects.filter(category_id=id)) #! for urun in urunler kısmı == kategori_urunler.html

    node = Category.objects.get(pk=id)
    children = Category.objects.add_related_count(node.get_children(), Product,
                                                  'category', 'product_counts')
    for dd in children:
        a = list(Product.objects.filter(category_id=dd.id))
        urunler.extend(a)

    context = {'page': 'Kategori',
               'urunKategori': urunKategori,
               'urunler': urunler}
    return render(request, 'kategori_urunler.html', context)

def productDetail(request, id, slug):
    urun = Product.objects.get(pk=id)
    images = Images.objects.filter(product=urun)
    # print(request.get_full_path())
    # print(request.get_host())
    # print(request.build_absolute_uri())
    comments = Comment.objects.filter(product_id=id)
    context = {'page': 'Urun',
               'urun': urun,
               'images': images,
               'comments': comments
               }
    return render(request, 'urun_detay.html', context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)
            context = {'urunler': products,
                       'query': query}
            return render(request, 'product_search.html', context)
    return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    category = Category.objects.all()
    if request.method == 'POST':  # check post
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                request.session['cart_items'] = ShopCart.objects.filter(user_id=user.id).count()
                messages.success(request, "Başarılı şekilde oturum açtınız {}".format(user.username))
                return HttpResponseRedirect('/login')
            else:
                messages.warning(request, "Girilen Bilgiler Hatalı Tekrar Deneyiniz {}".format(username))
                return HttpResponseRedirect('/login')
                
    form = LoginForm
    context = {'form': form}
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
            # sonradan eklenecek kısım
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')
            
    form = SignUpForm()
    context = {'form': form}
    return render(request, 'signup_form.html', context)

def userProfile_view(request):
    category = Category.objects.all()
    if request.method == 'POST':  # check post
        form = UserProfileForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/user_profile')
            
    form = UserProfileForm
    context = {'form': form}
    return render(request, 'userprofile.html', context)