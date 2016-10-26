from django.conf.urls import url

from Main.views import main

urlpatterns = [
    url(r'^/?$', main),
]