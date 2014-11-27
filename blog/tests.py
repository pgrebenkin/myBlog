from django.test import TestCase
from django.utils import timezone
from blog.models import Post, Label
# Create your tests here.

class PostTest(TestCase):
	def test_create_post(self):
		label = Label()
		label.name = 'python'
		label.save()
		post = Post()
		post.title = 'Test post'
		post.save()
		post.abstract = 'Test Abstract'
		post.body = 'Post Body'
		post.slug = 'test-post'
		post.label = [1]
		post.publish = True
		post.created = timezone.now()
		post.modified = timezone.now()
		post.numofseen = 0
		post.save()
		all_posts = Post.objects.all()
		self.assertEquals(len(all_posts), 1)
		only_post = all_posts[0]
		self.assertEquals(only_post, post)
		self.assertEquals(only_post.title, 'Test post')
		self.assertEquals(only_post.abstract, 'Test Abstract')
		self.assertEquals(only_post.body, post.body)
		self.assertEquals(only_post.slug, post.slug)
		self.assertEquals(only_post.label.get(), post.label.get())
		self.assertEquals(only_post.created.day, post.created.day)
		self.assertEquals(only_post.created.month, post.created.month)
		self.assertEquals(only_post.created.year, post.created.year)
		self.assertEquals(only_post.created.hour, post.created.hour)
		self.assertEquals(only_post.created.minute, post.created.minute)
		self.assertEquals(only_post.created.second, post.created.second)
		self.assertEquals(only_post.modified, post.modified)
		self.assertEquals(only_post.numofseen, 0)
class LabelTest(TestCase):
	def test_create_label(self):
		label = Label()
		label.name = 'python'
		label.save()
		all_labels = Label.objects.all()
		self.assertEquals(len(all_labels),1)
		only_label = all_labels[0]
		self.assertEquals(only_label.name, 'python')

