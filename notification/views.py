from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(
            utilisateur=self.request.user
        ).select_related('tache')

    @action(detail=True, methods=['patch'], url_path='marquer-lue')
    def marquer_lue(self, request, pk=None):
        notif = self.get_object()
        notif.est_lu = True
        notif.save()
        return Response({'message': 'Notification marquée comme lue'})

    @action(detail=False, methods=['patch'], url_path='tout-marquer-lues')
    def tout_marquer_lues(self, request):
        self.get_queryset().filter(est_lu=False).update(est_lu=True)
        return Response({'message': 'Toutes les notifications marquées comme lues'})