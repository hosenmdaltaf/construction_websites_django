from django.urls import path
from . import views
# from productapp.views import ProductDetailView

app_name='projectapp'

urlpatterns = [
    path('project/<int:pk>/', views.project_details, name='project_detailspage'),
    path('scope/<int:pk>/', views.scope_details, name='scope_detailspage'),
    
]