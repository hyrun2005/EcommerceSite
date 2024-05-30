from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


# Create your views her
def home_page_view(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'index.html', context=context)


def about_page(request):
    return render(request, 'about_page.html', {})


def categories(request, foo):
    foo = foo.replace("-", " ")
    try:
        category = Category.objects.get(name=foo)
        product = Product.objects.filter(category=category)

        context = {
            "category": category,
            "products": product,
        }
        return render(request, 'categories.html', context=context)
    except:
        messages.info(request, 'Category is not found!!!')
        return redirect('home')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'You have logged In successfully!!!')
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('login')
    else:
        template = 'login.html'
        context = {}
        return render(request, template, context=context)


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logout successfully!')
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Log In user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have registered successfully!!!')
            return redirect('home')
        else:
            messages.info(request, 'Ooops, there was a problem. Try again!.')
            return redirect('registrate')
    else:
        return render(request, 'register.html', {'form': form})


def product_info(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'product.html', context=context)
