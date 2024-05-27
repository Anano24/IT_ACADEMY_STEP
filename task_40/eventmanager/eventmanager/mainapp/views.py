from django.shortcuts import render, redirect
from .models import Attendee, Category, Event
from .forms import EventForm, AttendeeForm
from django.db.models import Q




def main_page(request):
    
    query = request.GET.get('query')
    if query:
        events = Event.objects.filter(Q(title__icontains=query) | Q(category__name__icontains=query))

    else:
        events = Event.objects.all()

    return render(request, 'index.html', {'events': events})



def add_event(request):

    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            event = form.save()
            return redirect('mainapp:main_page')
    else:
        form = EventForm()
        return render(request, 'add_event.html', {'form': form})
    


def add_attendee(request):

    if request.method == 'POST':
        form = AttendeeForm(request.POST)

        if form.is_valid():
            attendee = form.save()
            return redirect('mainapp:main_page')
    else:
        form = AttendeeForm()
        return render(request, 'add_attendee.html', {'form': form})
    


def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    attendees = Attendee.objects.filter(event_id=event_id)

    return render(request, 'event_detail.html', {'event': event, 'attendees': attendees})



def delete_attendee(request, attendee_id):
    attendee_for_delete = Attendee.objects.get(pk=attendee_id)
    event_id = attendee_for_delete.event.id
    attendee_for_delete.delete()

    return redirect('mainapp:event_detail', event_id)



def delete_event(request, event_id):
    event_for_delete = Event.objects.get(pk=event_id)
    event_for_delete.delete()

    return redirect('mainapp:main_page')


