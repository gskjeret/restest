from django.conf.urls import include, url

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view

from .views import VareprisCreateView, VareCreateView, OrdrestatusCreateView, OrdrelinjeCreateView, OrdreCreateView, LeverandorCreateView, KundeCreateView, KundetypeCreateView, FakturaCreateView, FakturalinjeCreateView, DebugMessagesCreateView
from .views import VareprisDetailsView, VareDetailsView, OrdrestatusDetailsView, OrdrelinjeDetailsView, OrdreDetailsView, LeverandorDetailsView, KundeDetailsView, KundetypeDetailsView, FakturaDetailsView, FakturalinjeDetailsView, DebugMessagesDetailsView

urlpatterns = {
    url(r'^customers/$', KundeCreateView.as_view(), name="create"),
    url(r'^customers/(?P<pk>[0-9]+)/$', KundeDetailsView.as_view(), name="details"),

    url(r'^orders/$', OrdreCreateView.as_view(), name="create"),
    url(r'^orders/(?P<pk>[0-9]+)/$', OrdreDetailsView.as_view(), name="details"),

    url(r'^orderlines/$', OrdrelinjeCreateView.as_view(), name="create"),
    url(r'^orderlines/(?P<pk>[0-9]+)/$', OrdrelinjeDetailsView.as_view(), name="details"),

    url(r'^products/$', VareCreateView.as_view(), name="create"),
    url(r'^products/(?P<pk>[0-9]+)/$', VareDetailsView.as_view(), name="details"),

    url(r'^suppliers/$', LeverandorCreateView.as_view(), name="create"),
    url(r'^suppliers/(?P<pk>[0-9]+)/$', LeverandorDetailsView.as_view(), name="details"),

    url(r'^swagger$', get_swagger_view(title='Restest API')),
    url(r'^swagger/$', get_swagger_view(title='Restest API'))
}

urlpatterns = format_suffix_patterns(urlpatterns)
