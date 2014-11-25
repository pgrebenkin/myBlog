from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns(
	'',
	url(r'^$',views.BlogIndex.as_view(), name = 'index'),
	url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name = 'entry_detail'),	
)