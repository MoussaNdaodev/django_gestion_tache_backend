from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProjectCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        # ✅ Lecture autorisée aux membres, écriture au créateur
        if request.method in SAFE_METHODS:
            return True
        return obj.createur == request.user