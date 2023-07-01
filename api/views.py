from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from api.models import Price, Product, Store

from api.serializers import PriceSerializer, ProductSerializer, StoreSerializer

class StoreViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Store.objects.all()
        serializer = StoreSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=StoreSerializer,
        responses={201: StoreSerializer},
    )
    def create(self, request):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            store = Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StoreSerializer(store)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            store = Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            store = Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StoreSerializer(store, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ProductSerializer,
        responses={201: ProductSerializer},
    )
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(user=user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(pk=self.kwargs['pk']).first()
        if not obj:
            raise Product.DoesNotExist
        self.check_object_permissions(self.request, obj)
        return obj


class PriceViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        queryset = Price.objects.all()
        serializer = PriceSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=PriceSerializer,
        responses={201: PriceSerializer},
    )
    def create(self, request):
        serializer = PriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            price = Price.objects.get(pk=pk)
        except Price.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PriceSerializer(price)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            price = Price.objects.get(pk=pk)
        except Price.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PriceSerializer(price, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            price = Price.objects.get(pk=pk)
        except Price.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PriceSerializer(price, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, pk=None):
        try:
            price = Price.objects.get(pk=pk)
        except Price.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        price.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)