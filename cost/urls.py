from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^expenses/', views.expense, name="expenses"),
    url(r'^add-expense/', views.add, name="add-expense"),
]
