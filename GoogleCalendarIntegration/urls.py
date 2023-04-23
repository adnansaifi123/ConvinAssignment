from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^rest/v1/calendar/init/', views.GoogleCalendarInitView.as_view(), name='GoogleCalendarInitView'),
    url(r'^rest/v1/calendar/redirect/', views.GoogleCalendarRedirectView.as_view(), name='GoogleCalendarRedirectView')
]