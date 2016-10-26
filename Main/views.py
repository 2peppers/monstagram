from django.shortcuts import render

from Main.models import Post


def main(request):
    return render(request, 'main.html', {'posts': Post.objects.all()})