from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, kunder, ordre, produkter, leverandorer
from .views import kunde_detalj, produkt_detalj, leverandor_detalj

urlpatterns = [
    url(r'home$', home, name="home"),
    url(r'login$', 
        LoginView.as_view(template_name="home/login_form.html"),
        name="home_login"),
    url(r'logout$', 
        LogoutView.as_view(),
        name="home_logout"),
    url(r'kunder$', kunder),
    url(r'ordre$', ordre),
    url(r'produkter$', produkter),
    url(r'leverandorer$', leverandorer),
    url(r'kunder/(?P<kid>\d+)/$', kunde_detalj, name="kunde_detalj"),
    url(r'produkter/(?P<pid>\d+)/$', produkt_detalj, name="produkt_detalj"),
    url(r'leverandorer/(?P<lid>\d+)/$', leverandor_detalj, name="leverandor_detalj"),
]
