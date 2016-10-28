from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User


from Main.models import Post, Like

@login_required
def main(request):
    all_posts = Post.objects.all()
    liked_posts_ids = [like.post.id for like in Like.objects.filter(user=request.user) if like.post in all_posts]

    return render(request, 'main.html', {'posts': all_posts, 'liked_posts_ids': liked_posts_ids,})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=int(post_id))
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
        return HttpResponse('-1')
    return HttpResponse('+1')


@login_required
def add_post(request):
    if request.method == 'POST':
        print(request.POST)
        title = request.POST.get('title', '')
        url_ = request.POST.get('url', '')
        image_file = request.POST.get('image_file', '')
        comments = request.POST.get('comments','')
        if title and (url_ or image_file):
            if Post.objects.filter(url=url_, title=title).count():
                context = dict(
                message = 'Bayan!<br/> [:|||||||||||||||||:]',
                message_type = 'danger',
                )
                return render(request, 'add_post.html', context)

            Post.objects.create(title=title, url=url_, comment=comments, author=request.user)
        else:
            context = dict(
                message='Empty TITLE or URL',
                message_type='danger',
            )
            return render(request, 'add_post.html', context)
        return HttpResponseRedirect(reverse('main'))

    else:
        return render(request, 'add_post.html', {})
