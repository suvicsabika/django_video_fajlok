from django.urls import path
from .views import hello, datas, data_input, person_form

urlpatterns = [
    path('hello/', hello, name='hello'),
    path("datas/", datas, name='datas'),
    path('data_input/', data_input, name='data_input'),
    path("person_form/", person_form, name='person_form')
]
