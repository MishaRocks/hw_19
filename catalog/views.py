from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from catalog.models import Product, Blogpost


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Новые товары',
        'about': 'Последние поступления товаров представлены ниже. Странно сформулировано, да?'
    }


def contacts(request):
    context = {
        'title': 'Наши контакты',
        'about': ''
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        show_product = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['object_list'] = Product.objects.get(pk=self.kwargs.get('pk')),
        context_data['title'] = f'В продаже: {show_product.name}'

        return context_data

class BlogpostCreateView(CreateView):
    model = Blogpost
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('catalog:index')


class BlogpostListView(ListView):
    model = Blogpost
    template_name = 'blogpost_list.html'


class BlogpostDetailView(DetailView):
    model = Blogpost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.showed += 1
        self.object.save()
        return self.object

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        show_product = Blogpost.objects.get(pk=self.kwargs.get('pk'))
        context_data['object_list'] = Blogpost.objects.get(pk=self.kwargs.get('pk')),

        return context_data
