from django.urls import path
from common.views import main, first_warm_up, fourth_orm_task

app_name = 'common'
urlpatterns = [
    path('', main, name='main'),
    path('warm_up/', first_warm_up, name='warm_up'),
    path('orm_task/', fourth_orm_task, name='orm_task'),
]