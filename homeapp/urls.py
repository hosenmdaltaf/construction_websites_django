from django.urls import path
from . import views
# from productapp.views import ProductDetailView

app_name='homeapp'

urlpatterns = [
    path('', views.home, name='homepage'),
    
]