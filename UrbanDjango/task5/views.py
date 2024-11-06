
from django.http import HttpResponse
from django.shortcuts import render
from django import forms


# Create your views here.


def sign_up_by_html(request):
    users = ['Anton', 'Mariya', 'Sergey']

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        info = {}
        context = {
            'error': info,
        }

        ex_user = [i for i in users if i == username]
        if ex_user:
            info['error'] = 'Пользователь уже существует'
            return render(request, 'registration_page.html', context, )

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', context)

        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, 'registration_page.html', context)

        print(f'Name: {username}')
        print(f'Password: {password}')
        print(f'Age: {age}')

        return HttpResponse(f'Приветствуем {username}')

    return render(request, 'registration_page.html')


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:')
    password = forms.CharField(max_length=8, label='Введите пароль:')
    repeat_password = forms.CharField(max_length=8, label='Повторите пароль:')
    age = forms.CharField(max_length=3, label='Введите свой возраст:')


def sign_up_by_django(request):
    users = ['Anton', 'Mariya', 'Sergey']

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            info = {}
            context = {
                'error': info,
            }

            ex_user = [i for i in users if i == username]
            if ex_user:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', context, )

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', context)

            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', context)

            print(f'Name: {username}')
            print(f'Password: {password}')
            print(f'Age: {age}')

            return HttpResponse(f'Приветствуем {username}')
    else:
        form = UserRegister()

    return render(request, 'registration_page.html', {'form': form})
