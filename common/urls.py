from django.urls import path
from common.views import main, first_warm_up

app_name = 'common'
urlpatterns = [
    path('', main, name='main'),
    path('warm_up/', first_warm_up, name='warm_up'),
]