from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from shop.models import Product
from .permissions import IsAdminTehran, IsBuyer
from .serializer import *
from rest_framework import views


# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['GET'], url_path="all_discount_products", url_name="all_discount_products",
            permission_classes=[AllowAny])
    def discount_products(self, request):
        min_discount = request.query_params.get('min_discount', 0)
        try:
            min_discount = int(min_discount)
        except ValueError:
            return Response({'error': 'Invalid value for min_discount'}, status=400)
        products = self.queryset.filter(off__gt=min_discount)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

class UserListAPLView(views.APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        users = ShopUser.objects.all()
        serializer = ShopUserSerializer(users, many=True)
        return Response(serializer.data)


class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = ShopUser.objects.all()
    serializer_class = UserRegisterSerializer

class OrderListAPLView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminTehran]

class OrderDtailAPIView(generics.RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsBuyer]