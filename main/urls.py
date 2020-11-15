from django.urls import path

from .views import home, about, services

urlpatterns = [
	path('services/',services,name='services-url'),
	path('about/', about, name='about-url'),
    path('', home, name='home-url'),
]
