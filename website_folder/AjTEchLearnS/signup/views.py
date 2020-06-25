from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def signup(request):
    return render(request,'login/signup.html')

# Authenticated API
def handlesignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check errorneous
        # username should be under 10 characters
        if len(username) > 10:
            messages.error(request,'Username must be under 10 character')
            # return redirect('home')
            return render(request,'login/signup.html')
        
        # username should be alphanumeric
        if not username.isalnum():
            messages.error(request,"Username should only contain alphanumeric")
            # return redirect('home')
            return render(request,'login/signup.html')
        
        # password matching
        if pass1 != pass2:
            messages.error(request,"Passwords do not match")
            # return redirect('home')
            return render(request,'login/signup.html')

        # elif User.objects.filter(username=username).exists():
        #     print('Username Taken')
        else:
            # Create the user
            user = User.objects.create_user(username,email,pass1)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request,"Your AjTEchLearnS account has been successfully created")
            print('user created')
            # return render(request,'success.html')
            return redirect('login')

    else:
        return render(request,'page_404/page_404_error.html')