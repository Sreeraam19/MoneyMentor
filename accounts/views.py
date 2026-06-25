from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user_model

# This safely gets your new Custom User model (AbstractUser)
User = get_user_model() 

def signup_view(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        f_name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        goal = request.POST.get('goal')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match. Please try again.")
            return redirect('signup')

        if User.objects.filter(username=u_name).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        # Create user directly with the new fields (No Profile needed)
        user = User.objects.create_user(
            username=u_name,
            first_name=f_name,
            email=email,
            password=pass1,
            date_of_birth=dob,
            financial_goal=goal
        )
        
        login(request, user)
        return redirect('home')
        
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(username=u_name, password=pass1)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials.")
            
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')
