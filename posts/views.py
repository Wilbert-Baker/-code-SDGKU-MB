from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post 
from django.urls import reverse_lazy

# Create your views here
"""
PostListView is going to retrieve all of the objects from the Post table in the db
"""
class PostListView(ListView):
    #template_name attribute is going to be to render
    template_name="post/list.html"
    #model is going to be from which table we want to
    model=Post
    #context is a python dictionary that hold the data
    #and this context travels to the htmls
    # by default the context name of listView and DetailLView"object" or "object_List"
    #context_object_name would allow us to modify that name and how to call it in  the htmls
    context_object_name="posts"

    """PostDetailView is going to retrieve a single element from the post table in the db
    """

class PostDetailView(DetailView):
    template_name="posts/detail.html"
    model=Post
    context_object_name="single_post"

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model=Post
    context_object_name="new_post"
    fields=["title", "subtitle", "body"]


    """
    PostUpdateView is going to allow us to edit existing records from the db
    """
class PostUpdateView(UpdateView):
    template_name="post/edit.html"
    model=Post
    fields = ["title", "subtitle", "body"]


"""
PostDeleteView is going to allowu us to delete an existing record from the db
"""
class PostDeleteView(DeleteView):
    template_name="post/delete.html"
    model=Post
    success_url= reverse_lazy("post_list")


# class PostDeleteView():


# class PostUpdateView():