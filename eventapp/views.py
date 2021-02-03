from django.shortcuts import render

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    user_profile= Profile.objects.filter(user=current_user.id).first()
    comment= Comment.objects.filter(user=current_user.id).first()
    event = Event.objects.all()

   
    return render(request, 'users/index.html', {'user_profile':user_profile, 'events':events,'comment':comment})


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
        searched_projects = Project.search_project(search_term)
        current_user=request.user
        message = f"{search_term}"
        return render(request, 'users/search.html',{"message":message,"titles": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'users/search.html',{"message":message})

def locations(request,location):
    locations = Event.filterimageByLocation(location)
    return render(request,'locations.html',{'locations':locations})

@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    events = Event.objects.filter(user=current_user).all()
    user_profile = Profile.objects.filter(user=current_user.id).first()
    

    return render(request, 'users/user_profile.html', { 'user_profile':user_profile,'events':events})
