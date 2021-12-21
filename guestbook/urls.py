from django.urls import path
from .views import GuestBookListView

urlpatterns = [
    path('', GuestBookListView.as_view(), name='home'),
]