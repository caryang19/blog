from django.shortcuts import render
from django.views.generic import ListViews
from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'