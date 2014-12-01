from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import render
# Create your models here.
class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)
class Label(models.Model):
	name = models.CharField(max_length=80, blank = True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Label'
		verbose_name_plural = 'Labels'
class Post(models.Model):
	title = models.CharField(max_length=200)
	abstract = models.TextField(max_length=300)
	body = models.TextField()
	slug= models.SlugField(max_length=200, unique = True)
	label = models.ManyToManyField(Label)
	publish = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	numofseen = models.PositiveIntegerField(blank = True, default = 0)
	objects = EntryQuerySet.as_manager()
	
	def get_absolute_url(self):
		return reverse("post_detail", kwargs = {"slug":self.slug})
	
	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = "Blog post"
		verbose_name_plural = "Blog posts"
		ordering = ["-created"]