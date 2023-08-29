from django.shortcuts import render
# from .forms import UserForm, UserProfileInfoForm
from django.http import HttpResponseRedirect, JsonResponse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



def user_auth(request):
    """this function will check to see if a user is authenticated, 
    and if so will return the user info in a dictionary"""
    user = get_user(request)
    if user and user.is_authenticated():
        response = {
            "id": user.id,
            "username": user.username,
            "firstName": user.first_name,
            "lastName": user.last_name,
            "lastLogin": user.last_login,
            "dateJoined": user.date_joined
        }
        return JsonResponse(response)

# need to test auth route but will want to refactor login first

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            
            else:
                print("Account not active!")
                # To Do: make an errors page to handle multiple issues
        
        else:
            print("Failed login attempt")
            print(f"Username: {username} tried to log in!")
            # To Do: error page stuff like above
    else:
        return render(request, "CIA_users/login.html")



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/') 


def user_signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
            print("New User Created!!")
            login(request, user)
            return HttpResponseRedirect('/')
        
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        return render(request, "CIA_users/signup.html", {
            'user_form': user_form, 
            'profile_form': profile_form, 
        })