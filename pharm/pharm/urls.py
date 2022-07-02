from django.urls import path

from pharm.apis.views import ProductListCreateAPIView,ProductRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('list/' , ProductListCreateAPIView.as_view(), name='list'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='byItem')
]