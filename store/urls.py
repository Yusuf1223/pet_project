from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('delivery/', views.delivery, name='delivery'),
    path('guarantee/', views.returns, name='guarantee'),
    path('privacy/', views.policy, name='privacy'),
    path('rights/', views.rights, name='rights'),
    path('about/', views.AboutView.as_view(), name='about')
]