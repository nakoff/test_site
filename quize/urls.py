from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$',views.post_list, name='post_list'),
	url(r'^user/add/$', views.add_user, name='add_user'),
	url(r'^user/add/(?P<pk>[а-яА-ЯёЁa-zA-Z0-9]+)/$', views.add_cat, name='add_cat'),
	url(r'^user/add/cont/(?P<pk>[а-яА-ЯёЁa-zA-Z0-9]+)/$', views.add_cont, name='add_cont'),
	url(r'^user/(?P<pk>[а-яА-ЯёЁa-zA-Z0-9]+)/$', views.user_detail, name='user_detail'),
]