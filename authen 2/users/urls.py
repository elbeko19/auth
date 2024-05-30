from django.urls import path, include
from django.views.generic import TemplateView
from users.views import Registration

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', Registration.as_view(), name='registration')
]

