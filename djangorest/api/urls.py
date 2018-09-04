from django.conf.urls import include, url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CustomersCreateView, CustomersDetailsView

urlpatterns = {
    url(r'^customers/$', CustomersCreateView.as_view(), name="create"),
    url(r'^customers/(?P<pk>[0-9]+)/$', CustomersDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
