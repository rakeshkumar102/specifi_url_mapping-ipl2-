from django.urls import path
from rcb.views import *
app_name='rcb_fans'

urlpatterns=[
    path('captain/',captain,name='faf')
]