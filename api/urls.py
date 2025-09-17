from django.urls import path,include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
app_name= 'api'

urlpatterns=[
    path('', include(router.urls)),
    path('users/', views.UserListAPLView.as_view(), name='user-list-api'),
    path('register/', views.UserRegistrationAPIView.as_view(), name='user-registration-api'),

]