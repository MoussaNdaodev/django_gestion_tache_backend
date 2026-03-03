from rest_framework import generics
from .models import Statistique, Prime
from .serializers import StatistiqueSerializer, PrimeSerializer

class StatistiqueListCreateView(generics.ListCreateAPIView):
    queryset = Statistique.objects.all()
    serializer_class = StatistiqueSerializer

class StatistiqueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statistique.objects.all()
    serializer_class = StatistiqueSerializer

class PrimeListCreateView(generics.ListCreateAPIView):
    queryset = Prime.objects.all()
    serializer_class = PrimeSerializer

class PrimeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prime.objects.all()
    serializer_class = PrimeSerializer
