from django.shortcuts import render

# Create your views here.


def main_page(request):
    title = 'Game Store'
    text = 'Welcome to our store'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'main_page.html', context)


def shop(request):
    title = 'Game Store'
    text = 'Select a game'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'shop.html', context)


def cart(request):
    title = 'Game Store'
    text = 'Your cart is empty'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'cart.html', context)
