from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, kunder, ordre, produkter, leverandorer
from .views import kunde_detalj, produkt_detalj, leverandor_detalj, ny_ordre

urlpatterns = [
    url(r'home$', home, name="home"),
    url(r'login$', 
        LoginView.as_view(template_name="home/login_form.html"),
        name="home_login"),
    url(r'logout$', 
        LogoutView.as_view(),
        name="home_logout"),
    url(r'kunder$', kunder, name="kunder"),
    url(r'ordre$', ordre, name="ordre"),
    url(r'produkter$', produkter, name="produkter"),
    url(r'leverandorer$', leverandorer, name="leverandorer"),
    url(r'kunder/(?P<kid>\d+)/$', kunde_detalj, name="kunde_detalj"),
    url(r'produkter/(?P<pid>\d+)/$', produkt_detalj, name="produkt_detalj"),
    url(r'leverandorer/(?P<lid>\d+)/$', leverandor_detalj, name="leverandor_detalj"),
    url(r'ny_ordre/(?P<kid>\d+)/$', ny_ordre, name="ny_ordre"),
]
