from django.urls import path, include

from rest_framework import routers
from . import views_api, views

app_name = 'backend_phm'


urlpatterns = [
    # path('', views_api.ApiRoot.as_view(),name=views_api.ApiRoot.name),
     # ---------------
    path('ini-api/',views.ini_api, name='ini-api'),
    path('test-electrical/turn-ratio', views_api.get_te_turn_ratio,name='get-te-turn-ratio'),

]