from django.conf.urls import include, url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CustomerCreateView, OrderCreateView, OrderLineCreateView, ProductCreateView, SupplierCreateView
from .views import CustomerDetailsView, OrderDetailsView, OrderLineDetailsView, ProductDetailsView, SupplierDetailsView

urlpatterns = {
    url(r'^customers/$', CustomerCreateView.as_view(), name="create"),
    url(r'^customers/(?P<pk>[0-9]+)/$', CustomerDetailsView.as_view(), name="details"),

    url(r'^orders/$', OrderCreateView.as_view(), name="create"),
    url(r'^orders/(?P<pk>[0-9]+)/$',OrderDetailsView.as_view(), name="details"),

    url(r'^orderlines/$', OrderLineCreateView.as_view(), name="create"),
    url(r'^orderlines/(?P<pk>[0-9]+)/$', OrderLineDetailsView.as_view(), name="details"),

    url(r'^products/$', ProductCreateView.as_view(), name="create"),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetailsView.as_view(), name="details"),

    url(r'^suppliers/$', SupplierCreateView.as_view(), name="create"),
    url(r'^suppliers/(?P<pk>[0-9]+)/$', SupplierDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
