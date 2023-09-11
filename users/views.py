from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm
from .models import User


def user_list(request):
    users = User.objects.all()
    return render(request, template_name='users_list.html', context={'users': users})


def add_user(request):
    form = UserForm
    return render(request, template_name='add_users.html', context={'form': form})


def save_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User saved")
    return HttpResponse("no info was provided to save")


def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return HttpResponse("Deletion Successful")
    except:
        return HttpResponse("Invalid ID")


def update_user(request, pk):
    try:
        user = User.objects.get(pk=pk)

        user.delete()
        form = UserForm
        return render(request, template_name='add_updated_user.html', context={'form': form, "pk": pk})
    except:
        return HttpResponse("Invalid ID")





