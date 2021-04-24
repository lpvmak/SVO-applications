
from rest_framework import generics, viewsets, status, mixins, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from . import models, serializers


class UserViewSet(viewsets.GenericViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['GET'], detail=False)
    def info(self, request, *args, **kwargs):
        ser = self.get_serializer(request.user)
        return Response(ser.data, status=status.HTTP_200_OK)
