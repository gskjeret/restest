from rest_framework import generics

from .models import Customer
from .serializers import CustomerSerializer


class CustomersCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new customer."""
        serializer.save()

class CustomersDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
