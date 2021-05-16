from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<int:pk>/', mainapp.products, name='index'),
    path('product/<int:pk>/', mainapp.product, name='product'),

]