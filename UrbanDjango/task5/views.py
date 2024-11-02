
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(f'Name: {username}')
        return HttpResponse('')
    return render(request, 'registration_page.html')

