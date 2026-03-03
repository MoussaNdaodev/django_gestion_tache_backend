from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Utilisateur
from .serializers import RegisterSerializer, ProfilSerializer

class RegisterView(generics.CreateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class ProfilView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfilSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user