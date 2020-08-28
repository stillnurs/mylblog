from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
	path('tags/', views.tag_list, name='tag_list'),
	path('tags<slug:slug>/', views.tag_detail, name='tag_detail'),
	path('', views.post_list, name='post_list'),
	path('gallery/', views.gallery_set, name='gallery-set'),
	path('<slug:post>/', views.post_detail, name='post_detail'),
]
