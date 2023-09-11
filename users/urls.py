from django.urls import path, include
from . import views


urlpatterns = [
    path('/list', views.user_list, name='user-list'),
    path('/add', views.add_user, name='add-user'),
    path('/delete/<int:pk>', views.delete_user, name='delete-user'),
    path('/update/<int:pk>', views.update_user, name='update-user'),
    path('/saved', views.save_user, name='save-user'),
]
