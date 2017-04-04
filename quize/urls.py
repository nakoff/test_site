from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$',views.post_list, name='post_list'),
	url(r'^user/add/$', views.add_user, name='add_user'),
	url(r'^user/(?P<pk>[а-яА-ЯёЁa-zA-Z0-9]+)/$', views.user_detail, name='user_detail'),
]