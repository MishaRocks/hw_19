from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, BlogpostCreateView, BlogpostListView, \
    BlogpostDetailView, BlogpostUpdateView, BlogpostDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    categories

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('new_post/', BlogpostCreateView.as_view(), name='new_post'),
    path('blog/', BlogpostListView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogpostDetailView.as_view(), name='post'),
    path('post/update/<int:pk>', BlogpostUpdateView.as_view(), name='update_post'),
    path('post/delete/<int:pk>', BlogpostDeleteView.as_view(), name='delete_post'),
    path('product/create/', ProductCreateView.as_view(), name='new_product'),
    path('product/create/<int:pk>', ProductUpdateView.as_view(), name='edit_product'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('categories/', categories, name='categories'),
]
