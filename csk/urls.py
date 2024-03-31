from django.urls import path
from csk.views import *
app_name='csk_fans'

urlpatterns=[
    path('captain/',captain,name='ruturaj'),
]