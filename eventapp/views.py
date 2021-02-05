from django.shortcuts import render,redirect
from .models import Profile,Event,Location
from django.db.models import Max,F
import datetime as dt
from .forms import NewProfileForm,NewEventForm,NewLocationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http  import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    user_profile= Profile.objects.filter(user=current_user.id).first()
    events = Event.objects.all()

   
    return render(request, 'users/index.html', {'user_profile':user_profile, 'events':events})


@login_required(login_url='/accounts/login/')
def new_event(request):
    current_user = request.user
  
    if request.method == 'POST':
        form = NewEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = current_user
            event.save()

        return redirect ("welcome")

    else:
        form = NewEventForm()

    return render(request, 'users/new_event.html', {"form": form})

def search_results(request):

    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_events = Event.search_event(search_term)
        current_user=request.user
        message = f"{search_term}"
        return render(request, 'users/search.html',{"message":message,"titles": searched_events})

    else:
        message = "You haven't searched for any term"
        return render(request, 'users/search.html',{"message":message})

def locations(request,location):
    locations = Event.filtereventByLocation(location)
    return render(request,'locations.html',{'locations':locations})

@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    events = Event.objects.filter(user=current_user).all()
    user_profile = Profile.objects.filter(user=current_user.id).first()
    

    return render(request, 'users/user_profile.html', { 'user_profile':user_profile,'events':events})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    
    if request.method == 'POST':
        form=NewProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect('user-profile')

    else:
            form=NewProfileForm()

    return render(request, 'users/edit_profile.html', {'form':form,})

@login_required(login_url='/accounts/login/')
def new_comment(request, project_id):
    current_user = request.user
    project = Project.objects.get(id=project_id)
    profile = Profile.objects.filter(user=current_user.id).first()
    if request.method == 'POST':
        form=NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.project=project
            comment.save()
            
            return redirect('welcome')

    else:
        form = NewCommentForm()

    return render(request, 'users/new_comment.html', {'form': form,'profile':profile, 'project':project, 'project_id':project_id})

