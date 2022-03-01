from django.urls import path
from .views import TestView
from .views import ResultView
urlpatterns = [
    path('test/',TestView.as_view(),name='test_list'),
    path('result/',ResultView.as_view(),name='result_list')
]
