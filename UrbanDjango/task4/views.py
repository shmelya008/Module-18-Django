from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def menu(request):
    title = 'Game Store'
    page_name = 'Main page'
    text = 'Welcome to our store'
    context = {
        'title': title,
        'text': text,
        'page_name': page_name
    }
    return render(request, 'menu.html', context)


def shop(request):
    title = 'Game Store'
    page_name = 'Games'
    text = 'Select a game'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'The Witcher 3']
    context = {
        'title': title,
        'page_name': page_name,
        'text': text,
        'games': games,
    }
    return render(request, 'shop.html', context)


def cart(request):
    title = 'Game Store'
    page_name = 'Cart'
    text = 'Your cart is empty'
    context = {
        'title': title,
        'page_name': page_name,
        'text': text
    }
    return render(request, 'cart.html', context)
