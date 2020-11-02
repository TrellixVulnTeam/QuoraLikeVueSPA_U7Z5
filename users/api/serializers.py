from rest_framework import serializers
from users.models import PersoUser
from rest_framework.authtoken.models import Token


class UserSerialzer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PersoUser

        fields = ["email", "username", "is_active", "is_admin", "token"]

    def get_token(self, instance):
        return Token.objects.get(user=instance).key

class AuthenticatedUserSerialzer(serializers.ModelSerializer):

    class Meta:
        model = PersoUser
        fields = ["username","ID"]

