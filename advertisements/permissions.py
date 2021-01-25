from rest_framework.permissions import BasePermission


class IsAuthorEntryOrStuff(BasePermission):
    """Автор объявления или админ"""

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user or request.user.is_staff
