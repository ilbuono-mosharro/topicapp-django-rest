from django.contrib.auth import get_user_model
from rest_framework import permissions, generics
from rest_framework.generics import CreateAPIView
from .permissions import IsOwner
from .serializers import UserSerializer

User = get_user_model()


class SignUp(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]