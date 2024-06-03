from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Category
from .forms import EventForm, RegistrationForm
from django.db.models import Q
from django.contrib.auth import logout, login


# Create your views here.


def main_page(request):
    query = request.GET.get('query')
    if query:
        events = Event.objects.filter(Q(title__icontains=query) | Q(category__name__icontains=query))
    else:
        events = Event.objects.all()

    if request.user.is_authenticated:
        events = events.exclude(attendee=request.user)

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



def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'event_detail.html', {'event': event})



def delete_event(request, event_id):
    event_for_delete = Event.objects.get(pk=event_id)
    event_for_delete.delete()

    return redirect('mainapp:main_page')



def attendee_profile(request):
    user_events = request.user.events_attendee.all()
    return render(request, 'attendee_profile.html', {'events': user_events})

    
def add_attendee(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.attendee.add(request.user)
    return redirect('mainapp:main_page')


def remove_attendee(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.user in event.attendee.all():
        event.attendee.remove(request.user)
    return redirect('mainapp:attendee_profile')



def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('mainapp:main_page')
        else:
            return render(request, 'registration/sign_up.html', {'form':form})
        
    else:
        form = RegistrationForm()
        return render(request, 'registration/sign_up.html', {'form':form})
    



def logout_user(request):
    logout(request)
    
    return redirect('mainapp:main_page')

