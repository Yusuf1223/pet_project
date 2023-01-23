from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from store.models import Info, Right, Contact, Order, Watch
from store.forms import FeedbackForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
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
    def get(self, request):
        about = Info.objects.get(key='about')
        form = FeedbackForm()
        contact = Contact.objects.get(pk=1)
        ctx = {'about': about, 'form': form, 'contact': contact}
        return render(request, 'store/about.html', ctx)

    def post(self, request):
        form = FeedbackForm(request.POST)
        about = request.GET.get('about')
        contact = request.GET.get('contact')
        ctx = {'about': about, 'form': form, 'contact': contact}

        if not form.is_valid():
            return render(request, 'store/about.html', ctx)

        form.save()
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

    # def post(self, request, pk):
    #     watch = Watch.objects.get(pk=pk)
    #     watch.count -= request.POST.


class WatchListView(ListView):
    model = Watch
    template_name = 'store/catalog.html'

