from django.urls import path
from . import views

app_name = 'tracker_app'

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('expense/add/', views.expense_create, name='expense_add'),
    path('expense/<int:pk>/edit/', views.expense_update, name='expense_edit'),
    path('expense/<int:pk>/delete/', views.expense_delete, name='expense_delete'),
    path('summary/', views.monthly_summary, name='monthly_summary'),
]