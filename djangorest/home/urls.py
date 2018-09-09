from django.conf.urls import url

from .views import home, kunder

urlpatterns = [
    url(r'home$', home),
    url(r'kunder$', kunder),
]
