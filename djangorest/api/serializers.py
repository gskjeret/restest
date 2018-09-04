from rest_framework import serializers

from .models import Customer, Order, OrderLine, Product, Supplier


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Customer
        fields = ('id', 'name', 'address1', 'address2', 'address3','postnr', 'poststed','phone','email','webpage')
        read_only_fields = ('id', 'id')

class OrderSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Order
        fields = ('id', 'customer_id','order_date','ship_date','total_cost','paid_date')
        read_only_fields = ('id', 'id')

class OrderLineSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = OrderLine
        fields = ('id', 'product_id','quantity','unit')
        read_only_fields = ('id', 'id')

class ProductSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Product
        fields = ('id', 'name','price','stock','supplier_id')
        read_only_fields = ('id', 'id')

class SupplierSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Supplier
        fields = ('id', 'name', 'address1', 'address2', 'address3','postnr', 'poststed','phone','email','webpage')
        read_only_fields = ('id', 'id')
