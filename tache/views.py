from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Tache
from .serializers import TacheSerializer

class MesTachesView(generics.ListAPIView):
    serializer_class = TacheSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        statut = self.request.query_params.get('statut')
        queryset = Tache.objects.filter(assigne_a=self.request.user)

        if statut:
            queryset = queryset.filter(statut=statut)

        return queryset


class TacheCreateView(generics.CreateAPIView):
    serializer_class = TacheSerializer
    permission_classes = [IsAuthenticated]