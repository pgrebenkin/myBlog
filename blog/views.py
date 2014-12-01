from django.shortcuts import render
from django.views import generic
from blog import models
# Create your views here.

class PostIndex(generic.ListView):
	queryset = models.Post.objects.published()
	template_name = "home.html"
	paginate_by = 10
class PostDetail(generic.DetailView):
	model = models.Post
	template_name = "post.html"
	