from django.urls import path
from . import views


app_name = 'mainapp'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('add_event/', views.add_event, name='add_event'),
    path('event_detail/<int:event_id>', views.event_detail, name='event_detail'),
    path('delete_event/<int:event_id>', views.delete_event, name='delete_event'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_user, name='logout_user'),
    path('add_attendee/<int:event_id>', views.add_attendee, name='add_attendee'),
    path('profile/', views.attendee_profile, name='attendee_profile'),
    path('remove_attendee/<int:event_id>', views.remove_attendee, name='remove_attendee')
]