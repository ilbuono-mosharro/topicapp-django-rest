from rest_framework.permissions import BasePermission


class IsOwnerUser(BasePermission):
    """
    Allows access only to Owner users.
    """

    def has_object_permission(self, request, view, obj):
        return bool(obj.starter == request.user)