from django.urls import LocalePrefixPattern
from . import views

urlpatterns = [
  path('login/', views.login, name = 'login'),
]