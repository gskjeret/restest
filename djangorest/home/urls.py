from django.conf.urls import url

from .views import home, kunder, ordre, produkter, leverandorer
from .views import kunde_detalj, produkt_detalj

urlpatterns = [
    url(r'home$', home),
    url(r'kunder$', kunder),
    url(r'ordre$', ordre),
    url(r'produkter$', produkter),
    url(r'leverandorer$', leverandorer),
    url(r'kunder/(?P<kid>\d+)/$', kunde_detalj, name="kunde_detalj"),
    url(r'produkter/(?P<pid>\d+)/$', produkt_detalj, name="produkt_detalj"),
]
