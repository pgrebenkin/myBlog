from django.test import TestCase, LiveServerTestCase, Client
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
class AdminTest(LiveServerTestCase):
	fixtures = ['users.json']
	def setUp(self):
		self.client = Client()
	def test_login(self):
		response = self.client.get('/admin/', follow=True)
		self.assertEquals(response.status_code, 200)
		self.assertTrue(str.encode('Log in') in response.content)
		self.client.login(username = 'test', password = 'test')
		response = self.client.get('/admin/')
		self.assertEquals(response.status_code, 200)
		self.assertTrue(str.encode('Log out') in response.content)
	def test_logout(self):
		self.client.login(username = 'test', password = 'test')
		response = self.client.get('/admin/')
		self.assertEquals(response.status_code, 200)
		self.assertTrue(str.encode('Log out') in response.content)
		self.client.logout()
		response = self.client.get('/admin/', follow=True)
		self.assertEquals(response.status_code, 200)
		self.assertTrue(str.encode('Log in') in response.content)
	def test_create_post(self):
		self.client.login(username = 'test', password = 'test')
		response = self.client.get('/admin/blog/post/add/')
		self.assertEquals(response.status_code, 200)
	def test_create_post(self):
		label = Label()
		label.name = 'winter'
		label.save()
		self.client.login(username = 'test', password = 'test')
		response = self.client.get('/admin/blog/post/add/')
		self.assertEquals(response.status_code, 200)
		response = self.client.post('/admin/blog/post/add/', {
			'title':'My test Post',
			'abstract':'Test Abstract',
			'body':'Test Post Body',
			'created':'2014-12-01',
			'modified':'2014-12-01',
			'slug':'my-test-post',
			'label':str(label.pk),
			'numofseen':str(0)
			},
			follow = True
			)
		self.assertEquals(response.status_code,200)
		self.assertTrue(str.encode('added successfully') in response.content)
		all_posts = Post.objects.all()
		self.assertEquals(len(all_posts),1)
	def test_edit_post(self):
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

		self.client.login(username = 'test', password = 'test')
		

		response = self.client.post('/admin/blog/post/'+str(post.pk)+'/', {
			'title':'second test post',
			'abstract':'second test abstract',
			'body':'second test body',
			'label':str(label.pk),
			'slug':'second-test-post',
			'numofseen':str(0)
			},
			follow = True
			)
		self.assertEquals(response.status_code,200)
		self.assertTrue(str.encode('changed successfully') in response.content)
		all_posts = Post.objects.all()
		self.assertEquals(len(all_posts), 1)
		only_post = all_posts[0]
		self.assertEquals(only_post.title, 'second test post')
		self.assertEquals(only_post.body, 'second test body')
	def test_delete_post(self):
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
		self.assertEquals(len(all_posts),1)
		self.client.login(username = 'test', password = 'test')
		response = self.client.post('/admin/blog/post/'+str(post.pk)+'/delete/',{
			'post':'yes'}, follow = True)
		self.assertEquals(response.status_code,200)
		self.assertTrue(str.encode('deleted successfully') in response.content)
		all_posts = Post.objects.all()
		self.assertEquals(len(all_posts),0)
		

