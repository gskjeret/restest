from rest_framework import generics

from .models import Customer, Order, OrderLine, Product, Supplier
from .serializers import CustomerSerializer, OrderSerializer, OrderLineSerializer, ProductSerializer, SupplierSerializer


class CustomerCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        serializer.save()

class OrderCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save()

class OrderLineCreateView(generics.ListCreateAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer

    def perform_create(self, serializer):
        serializer.save()

class ProductCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()

class SupplierCreateView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def perform_create(self, serializer):
        serializer.save()

class CustomerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
   
class OrderDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
   
class OrderLineDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
   
class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   
class SupplierDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
   
