from django.shortcuts import render

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    user_profile= Profile.objects.filter(user=current_user.id).first()
    comment= Comment.objects.filter(user=current_user.id).first()
    event = Event.objects.all()

   
    return render(request, 'users/index.html', {'user_profile':user_profile, 'events':events,'comment':comment})
