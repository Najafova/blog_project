from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *



urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('login/', login_view, name='login_view'),
    path('user_account/', user_account, name="user_account"),
    path('logout/', logout_view, name="logout-view"),
    path('post/<int:pk>/', detail_article, name="detail-article"),
    path('blog/new/', add_blog, name="add-blog"),
    path('blog/<int:pk>/edit/', edit_blog, name="edit-blog"),
    path('test/', test, name="test"),
    path('blog/<int:pk>/delete/', delete_blog, name="delete-blog"),
    path('change-password/', change_password, name="change_password"),

]