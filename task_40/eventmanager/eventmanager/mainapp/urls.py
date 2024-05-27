from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('add_event/', views.add_event, name='add_event'),
    path('add_attendee/', views.add_attendee, name='add_attendee'),
    path('event_detail/<int:event_id>', views.event_detail, name='event_detail'),
    path('delete_attendee/<int:attendee_id>', views.delete_attendee, name='delete_attendee'),
    path('delete_event/<int:event_id>', views.delete_event, name='delete_event')
]