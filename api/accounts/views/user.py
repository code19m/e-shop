from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from apps.accounts.models.user import User
from api.accounts.serializers.user import RegisterUserSerializer


class RegisterUserView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
