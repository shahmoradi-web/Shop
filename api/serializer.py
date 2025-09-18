from rest_framework import serializers
from shop.models import Product, ProductFeature,Category
from account.models import ShopUser
from orders.models import Orders

class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = ['name','value']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    features = ProductFeatureSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'new_price', 'features', 'category']

class ShopUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = ['id','username','first_name', 'last_name','email']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = ['phone','first_name', 'last_name', 'address', 'password']
    extra_kwargs = {
        'password': {'write_only': True}
    }

    def create(self, validated_data):
        user = ShopUser(phone=validated_data['phone'], first_name=validated_data['first_name'],
                        last_name=validated_data['last_name'],
                        address=validated_data['address'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
