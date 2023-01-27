from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from store.models import *
from store.forms import FeedbackForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    ctx = {'slide_list': ["img/slider/1.webp", "img/slider/2.webp", "img/slider/3.webp"]}
    return render(request, 'store/index.html', ctx)


def delivery(request):
    info = Info.objects.get(key='delivery')
    ctx = {'delivery': info}
    return render(request, 'store/delivery.html', ctx)


def returns(request):
    info = Info.objects.get(key='returns')
    ctx = {'returns': info}
    return render(request, 'store/guarantee.html', ctx)


def policy(request):
    info = Info.objects.get(key='policy')
    ctx = {'policy': info}
    return render(request, 'store/privacy.html', ctx)


def rights(request):
    right = Right.objects.get(pk=1)
    ctx = {'right': right}
    return render(request, 'store/rights.html', ctx)


class AboutView(View):
    about = Info.objects.get(key='about')
    contact = Contact.objects.get(pk=1)

    def get(self, request):
        form = FeedbackForm()
        ctx = {'about': self.about, 'form': form, 'contact': self.contact}
        return render(request, 'store/about.html', ctx)

    def post(self, request):
        form = FeedbackForm(request.POST)
        ctx = {'about': self.about, 'form': form, 'contact': self.contact}

        if form.is_valid():
            feedback = form.save()
            feedback.save()

        return render(request, 'store/about.html', ctx)


class CartListView(ListView, LoginRequiredMixin):
    model = Order
    template_name = 'store/cart.html'

    def get_queryset(self):
        qs = super(CartListView, self).get_queryset()
        return qs.filter(status='in_cart', user=self.request.user)


class WatchDetailView(DetailView):
    model = Watch
    template_name = 'store/product.html'

    def get_context_data(self, **kwargs):
        context = super(WatchDetailView, self).get_context_data(**kwargs)
        context['loop_times'] = range(2, context['watch'].count + 1)
        return context

    """Posting of form that store item into Cart and remove from Watches"""

    def post(self, request, pk):
        amount = request.POST.get('amount')
        watch = Watch.objects.get(pk=pk)
        watch.count -= int(amount)
        order = Order.objects.get_or_create(watch_id=pk, user_id=request.user.id, status='in_cart')
        order[0].count += int(amount)
        order[0].save()
        watch.save()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class WatchListView(ListView):
    model = Watch
    template_name = 'store/catalog.html'

    def get(self, request):
        watch_list = Watch.objects.all()

        """Filtering"""
        watch_color = request.GET.get('watch_color')
        bracelet_color = request.GET.get('bracelet_color')
        bracelet_material = request.GET.get('bracelet_material')
        watch_material = request.GET.get('watch_material')
        glass_material = request.GET.get('glass_material')
        max = request.GET.get('max')
        min = request.GET.get('min')

        """Searching"""
        strval = request.GET.get("search", False)

        if strval:
            query = Q(title__icontains=strval)
            watch_list = watch_list.filter(query)

        """Sorting"""
        sort = request.GET.get('sort')

        if sort == 1:
            watch_list = watch_list.order_by('-created_at')
        elif sort == 2:
            watch_list = watch_list.order_by('-price')

        """Filtering"""
        if watch_color:
            watch_list = watch_list.filter(watch_color__title=watch_color)
        if bracelet_color:
            watch_list = watch_list.filter(bracelet_color__title=bracelet_color)
        if watch_material:
            watch_list = watch_list.filter(watch_material__title=watch_material)
        if bracelet_material:
            watch_list = watch_list.filter(bracelet_material__title=bracelet_material)
        if glass_material:
            watch_list = watch_list.filter(glass_material__title=glass_material)
        if max and min:
            watch_list = watch_list.filter(price__range=(min, max))

        """ filter_list is needed for display all color, materials, and glass in filter"""
        filter_list = {'colors': Color.objects.all,
                       'materials': Material.objects.all,
                       'glass_materials': GlassMaterial.objects.all}

        ctx = {'watch_list': watch_list, 'filter_list': filter_list, 'search': strval}
        return render(request, 'store/catalog.html', ctx)
