from rest_framework import serializers
from apps.accounts.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username", 
            "password", 
            "first_name", 
            "last_name",
            "second_name",
            "phone_number",
            "image",
        )

        extra_kwargs = {
            "password": {"write_only": True},
        }
