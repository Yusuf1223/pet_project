from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'store'

urlpatterns = [
    path('', TemplateView.as_view(template_name='store/base.html'), name='index'),
    path('delivery/', views.delivery, name='delivery'),
    path('guarantee/', views.returns, name='guarantee'),
    path('privacy/', views.policy, name='privacy'),
    path('rights/', views.rights, name='rights'),
    path('about/', views.AboutView.as_view(), name='about')
]