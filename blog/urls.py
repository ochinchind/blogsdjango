
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_blog, name='hello_blog'),
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
]