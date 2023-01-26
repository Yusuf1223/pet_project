from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('delivery/', views.delivery, name='delivery'),
    path('guarantee/', views.returns, name='guarantee'),
    path('privacy/', views.policy, name='privacy'),
    path('rights/', views.rights, name='rights'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('cart/', views.CartListView.as_view(), name='cart'),
    path('product/<int:pk>', views.WatchDetailView.as_view(), name='watch'),
    path('catalog/', views.WatchListView.as_view(), name='catalog')
]