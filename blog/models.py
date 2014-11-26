from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)
class Tag(models.Model):
	name = models.CharField(max_length=80, blank = True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'
	#name = models.ForeignKey('Entry',related_name='label', related_query_name='label')
class Entry(models.Model):
	title = models.CharField(max_length=200)
	abstract = models.CharField(max_length=200)
	body = models.TextField()
	slug= models.SlugField(max_length=200, unique = True)
	tag = models.ManyToManyField(Tag)
	rank = models.PositiveIntegerField(default=0)
	publish = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	objects = EntryQuerySet.as_manager()
	def get_absolute_url(self):
		return reverse("entry_detail", kwargs = {"slug":self.slug})
	def __str__(self):
		return self.title
	def rank_add(self):
		self.rank+=1
		return reverse("entry_detail", kwargs = {"slug":self.slug})
	class Meta:
		verbose_name = "Blog entry"
		verbose_name_plural = "Blog entries"
		ordering = ["-created"]