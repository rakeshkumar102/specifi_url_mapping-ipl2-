from django.urls import path
from srh.views import *
app_name='srh_fans'

urlpatterns=[
    path('captain/',captain,name='cummins'),
]