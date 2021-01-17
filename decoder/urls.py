from django.urls import path
from .views import FixVersionView

urlpatterns = [
    path('', FixVersionView.as_view(), name='home'),
]