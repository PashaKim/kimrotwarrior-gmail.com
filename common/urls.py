from django.urls import path
from common.views import main, first_warm_up, second_regular_expressions, third_algorithms, fourth_orm_task

app_name = 'common'
urlpatterns = [
    path('', main, name='main'),
    path('warm_up/', first_warm_up, name='warm_up'),
    path('regular_expressions/', second_regular_expressions, name='regular_expressions'),
    path('algorithms/', third_algorithms, name='algorithms'),
    path('orm_task/', fourth_orm_task, name='orm_task'),
]