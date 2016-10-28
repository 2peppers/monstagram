from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User


from Main.models import Post, Like

@login_required
def main(request):
    all_posts = Post.objects.all()
    liked_posts_ids = [like.post.id for like in Like.objects.filter(user=request.user) if like.post in all_posts]

    return render(request, 'main.html', {'posts': all_posts, 'liked_posts_ids': liked_posts_ids,})


def like_post(request, post_id):
    post = get_object_or_404(Post, id=int(post_id))
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()

    return HttpResponseRedirect('/')
