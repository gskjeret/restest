from rest_framework import generics

from .models import Varepris, Vare, Ordrestatus, Ordrelinje, Ordre, Leverandor, Kunde, Kundetype, Faktura, Fakturalinje, DebugMessages
from .models import v_ordrelinje
from .serializers import VareprisSerializer, VareSerializer, OrdrestatusSerializer, OrdrelinjeSerializer, OrdreSerializer, LeverandorSerializer, KundeSerializer, KundetypeSerializer, FakturaSerializer, FakturalinjeSerializer, DebugMessagesSerializer
from .serializers import v_ordrelinjeSerializer

class VareprisCreateView(generics.ListCreateAPIView):
    queryset = Varepris.objects.all()
    serializer_class = VareprisSerializer
    def perform_create(self, serializer):
        serializer.save()

class VareCreateView(generics.ListCreateAPIView):
    queryset = Vare.objects.all()
    serializer_class = VareSerializer
    def perform_create(self, serializer):
        serializer.save()

class OrdrestatusCreateView(generics.ListCreateAPIView):
    queryset = Ordrestatus.objects.all()
    serializer_class = OrdrestatusSerializer
    def perform_create(self, serializer):
        serializer.save()

class OrdreCreateView(generics.ListCreateAPIView):
    queryset = Ordre.objects.all()
    serializer_class = OrdreSerializer
    def perform_create(self, serializer):
        serializer.save()

class OrdrelinjeCreateView(generics.ListCreateAPIView):
    queryset = Ordrelinje.objects.all()
    serializer_class = OrdrelinjeSerializer
    def perform_create(self, serializer):
        serializer.save()

class OrdrelinjeFilterView(generics.ListCreateAPIView):
    queryset = v_ordrelinje.objects.all()
    serializer_class = v_ordrelinjeSerializer
    def get_queryset(self):
        """
        Optionally restricts the returned orderlines to a given order,
        by filtering against a `order` query parameter in the URL.
        """
        queryset = v_ordrelinje.objects.all()
        p_order = self.request.query_params.get('order', None)
        if p_order is not None:
            queryset = queryset.filter(ordre=p_order)
        return queryset

class LeverandorCreateView(generics.ListCreateAPIView):
    queryset = Leverandor.objects.all()
    serializer_class = LeverandorSerializer
    def perform_create(self, serializer):
        serializer.save()

class KundeCreateView(generics.ListCreateAPIView):
    queryset = Kunde.objects.all()
    serializer_class = KundeSerializer
    def perform_create(self, serializer):
        serializer.save()

class KundetypeCreateView(generics.ListCreateAPIView):
    queryset = Kundetype.objects.all()
    serializer_class = KundetypeSerializer
    def perform_create(self, serializer):
        serializer.save()

class FakturalinjeCreateView(generics.ListCreateAPIView):
    queryset = Fakturalinje.objects.all()
    serializer_class = FakturalinjeSerializer
    def perform_create(self, serializer):
        serializer.save()

class FakturaCreateView(generics.ListCreateAPIView):
    queryset = Faktura.objects.all()
    serializer_class = FakturaSerializer
    def perform_create(self, serializer):
        serializer.save()

class DebugMessagesCreateView(generics.ListCreateAPIView):
    queryset = DebugMessages.objects.all()
    serializer_class = DebugMessagesSerializer
    def perform_create(self, serializer):
        serializer.save()


class VareprisDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Varepris.objects.all()
    serializer_class = VareprisSerializer

class VareDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vare.objects.all()
    serializer_class = VareSerializer

class OrdrestatusDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ordrestatus.objects.all()
    serializer_class = OrdrestatusSerializer

class OrdreDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ordre.objects.all()
    serializer_class = OrdreSerializer

class OrdrelinjeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ordrelinje.objects.all()
    serializer_class = OrdrelinjeSerializer


class LeverandorDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Leverandor.objects.all()
    serializer_class = LeverandorSerializer

class KundeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kunde.objects.all()
    serializer_class = KundeSerializer

class KundetypeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kundetype.objects.all()
    serializer_class = KundetypeSerializer

class FakturalinjeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fakturalinje.objects.all()
    serializer_class = FakturalinjeSerializer

class FakturaDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faktura.objects.all()
    serializer_class = FakturaSerializer

class DebugMessagesDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DebugMessages.objects.all()
    serializer_class = DebugMessagesSerializer
