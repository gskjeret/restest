"""Import serializers from the REST framework"""
from rest_framework import serializers

from .models import Varepris, Vare, Ordrestatus, Ordrelinje, Ordre, Leverandor, Kunde, Kundetype, Faktura, Fakturalinje, DebugMessages
from .models import v_ordrelinje

class DebugMessagesSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = DebugMessages
        fields = ('__all__')
        read_only_fields = [('line_id ')]

class FakturaSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Faktura
        fields = ('__all__')
        read_only_fields = [('faktura_id ')]

class FakturalinjeSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Fakturalinje
        fields = ('__all__')
        read_only_fields = [('faktura_id')]

class KundeSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Kunde
        fields = ('__all__')
        read_only_fields = [('kunde_id ')]

class KundetypeSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Kundetype
        fields = ('__all__')
        read_only_fields = [('kundetype_kode')]

class LeverandorSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Leverandor
        fields = ('__all__')
        read_only_fields = [('leverandor_id ')]

class OrdreSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Ordre
        fields = ('__all__')
        read_only_fields = [('ordre_id')]

class OrdrelinjeSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Ordrelinje
        fields = ('__all__')
        read_only_fields = [('ordre_id ')]

class OrdrestatusSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Ordrestatus
        fields = ('__all__')

class VareSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Vare
        fields = ('__all__')
        read_only_fields = [('produkt_id')]

class VareprisSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Varepris
        fields = ('__all__')
        read_only_fields = [('produkt_id')]

class v_ordrelinjeSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = v_ordrelinje
        fields = ('__all__')        


