from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from .forms import CommentForm
from .models import Post, Tag


# Create your views here.


def post_list(request):
	post = Post.published.all()
	latest_posts = Post.published.order_by('-created')[:3]
	pages_data = Paginator(post, 4)
	page_number = request.GET.get('page', 1)
	page = pages_data.get_page(page_number)
	is_paginated = page.has_other_pages()
	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''
	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''
	context = {
		'latest_posts': latest_posts,
		'post_data': page,
		'is_paginated': is_paginated,
		'next_url': next_url,
		'prev_url': prev_url,
	}
	return render(request, 'list.html', context)


def post_detail(request, post):
	post = get_object_or_404(Post, slug=post, status='published')
	comments = post.comments.filter(active=True)
	latest_posts = Post.published.order_by('-created')[:3]
	new_comment = None

	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
	else:
		comment_form = CommentForm()
	context = {
		'latest_posts': latest_posts,
		'post': post,
		'comments': comments,
		'new_comment': new_comment,
		'comment_form': comment_form,
	}

	return render(request, 'detail.html', context)


def tag_list(request):
	tags = Tag.objects.all()
	latest_posts = Post.published.order_by('-created')[:3]
	return render(request, 'tag_list.html', context={
		'latest_posts': latest_posts, 'tags': tags})


def tag_detail(request, slug):
	tag = get_object_or_404(Tag, slug__iexact=slug)
	latest_posts = Post.published.order_by('-created')[:3]
	context = {
		'tags': tag,
		'latest_posts': latest_posts,
	}
	return render(request, 'tag_detail.html', context)


def gallery_set(request):
	return render(request, 'gallery.html')
