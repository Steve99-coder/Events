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
