from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow staff and superuser for write request else read-only.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
        # Permissions for write request
        return bool(request.user and request.user.is_staff)
