from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns(
	'',
	url(r'^$',views.PostIndex.as_view(), name = 'index'),
	url(r'^(?P<slug>\S+)$', views.PostDetail.as_view(), name = 'post_detail'),	
)