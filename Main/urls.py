from django.conf.urls import url, include


from Main.views import main, like_post, add_post


urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^like/(\d+)/?$', like_post, name='like_post'),
    url(r'^add/?$', add_post, name='add_post')
]