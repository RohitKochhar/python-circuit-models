from django.urls import path

from . import views

urlpatterns = [
    path('',                    views.index,                    name='index'),
    path('rc-lowpass-filter/',  views.RCLowPassFilterDetail,    name='RCLowPassFilterDetail'),

]