from django.urls import path
from .views import home,development,contact,consult,training


urlpatterns = [
	path('consult/',consult,name='consult_url'),
	path('contact/',contact,name='contact_url'),
	path('training/',training,name='training_url'),
	path('development/',development,name='development_url'),
    path('',home,name='home_url')
]