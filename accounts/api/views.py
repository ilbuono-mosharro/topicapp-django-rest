from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsOwner
from .serializers import UserSerializer

User = get_user_model()


class SignUp(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated, IsOwner])
def user_detail(request):
    user = request.user.id
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = User.objects.get(id=user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == 'DELETE':
        user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        # Remove the token from the user's request object
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)