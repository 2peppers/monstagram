from django.conf.urls import url, include


from Main.views import main, like_post


urlpatterns = [
    url(r'^/?$', main),
    url(r'like/(\d+)/?$', like_post)
]