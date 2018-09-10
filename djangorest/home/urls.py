from django.conf.urls import url

from .views import home, kunder, ordre, produkter, leverandorer

urlpatterns = [
    url(r'home$', home),
    url(r'kunder$', kunder),
    url(r'ordre$', ordre),
    url(r'produkter$', produkter),
    url(r'leverandorer$', leverandorer),
]
