from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Blogpost, Version, Category
from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from catalog.services import get_some_cache


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
        context_data['object_list'] = show_product,
        context_data['actual_version'] = Version.objects.filter(sign=True)
        context_data['title'] = f'В продаже: {show_product.name}'

        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save()
        self.object.user_id = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    permission_required = 'catalog.change_product', 'catalog.view_product'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object


    def get_success_url(self):
        return reverse('catalog:product', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_staff and user.has_perm(self.permission_required):
            context_data['form'] = ProductModeratorForm
            return context_data

        versionformset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = versionformset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = versionformset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


class BlogpostCreateView(CreateView):
    model = Blogpost
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)


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

class BlogpostUpdateView(UpdateView):
    model = Blogpost
    fields = ('title', 'content', 'preview', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:post', args=[self.object.pk])


class BlogpostDeleteView(DeleteView):
    model = Blogpost
    success_url = reverse_lazy('catalog:blog')


# class CategoryListView(ListView):
#     model = Category
#     template_name = 'catalog/category_list.html'
#     extra_context = {
#         'title': 'Список категорий'
#     }
#     def get_context_data(self, *args, **kwargs):
#         context_data = super().get_context_data(*args, **kwargs)
#
#         show_product = Category.objects.get(pk=self.kwargs.get('pk'))
#         context_data['object_list'] = get_some_cache(Category),
#         context_data['title'] = 'Список категорий'
#
#         return context_data


def categories(request):
    context = {
        'object_list': get_some_cache(Category),
        'title': 'Список категорий'
    }
    return render(request, 'catalog/categories.html', context)