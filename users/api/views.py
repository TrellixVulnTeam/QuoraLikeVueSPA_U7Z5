from .serializers import UserSerialzer,AuthenticatedUserSerialzer
from rest_framework.generics import ListAPIView
from users.models import PersoUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class UserList(ListAPIView):
    queryset = PersoUser.objects.all()
    serializer_class = UserSerialzer
    permission_classes = [permissions.IsAdminUser]

class AuthenticatedUser(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,format=None):
        queryset = self.request.user
        serializer =AuthenticatedUserSerialzer(queryset)

        return Response(serializer.data)
