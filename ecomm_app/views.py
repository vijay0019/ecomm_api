from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from django.utils import timezone
from ecomm_app.models import Product
from ecomm_app.serializers import ProductSerializer, UserSerializer
from django.contrib.auth.models import User
from ecomm_app.permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, created_at=timezone.now())

    def perform_update(self, serializer):
        if 'active' in serializer.validated_data and not serializer.validated_data['active']:
            instance = self.get_object()
            instance.deleted_at = timezone.now()
            instance.active = False
            instance.save()
        else:
            serializer.save(updated_at=timezone.now())

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.active:
            instance.deleted_at = timezone.now()
            instance.active = False
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)