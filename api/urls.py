'''TBD'''
from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.bling_auth, name='bling_auth'),
    path('callback/', views.bling_callback, name='bling_callback'),
    path('import/', views.import_data, name='import_data'),
]
