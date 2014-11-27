from django.shortcuts import render
from django.views import generic
from blog import models
# Create your views here.

class BlogIndex(generic.ListView):
	queryset = models.Post.objects.published()
	template_name = "home.html"
	paginate_by = 10
class BlogDetail(generic.DetailView):
	model = models.Post
	template_name = "post.html"
	