from django.urls import path
from . import views
# from productapp.views import ProductDetailView

app_name='homeapp'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('cat/<int:pk>/', views.category_filter, name='categorypage'),
    path('product/', views.product, name='product_page'),
    path('product/<int:pk>/', views.product_details, name='product_detailspage'),
    path('who_we_are/', views.who_we_are, name='who_we_are_page'),
    path('who_we_are_for/', views.who_we_are_for, name='who_we_are_for_page'),  
    
]