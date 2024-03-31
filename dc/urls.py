from django.urls import path
from dc.views import *
app_name='dc_fans'

urlpatterns=[
    path('captain/',captain,name='pant')
]