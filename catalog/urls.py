from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, BlogpostCreateView, BlogpostListView, \
    BlogpostDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('new_post/', BlogpostCreateView.as_view(), name='new_post'),
    path('blog/', BlogpostListView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogpostDetailView.as_view(), name='post'),
]
