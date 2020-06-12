from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def signup(request):
    return render(request,'signup.html')

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
            return redirect('home')
        
        # username should be alphanumeric
        if not username.isalnum():
            messages.error(request,"Username should only contain alphanumeric")
            return redirect('home')
        
        # password matching
        if pass1 != pass2:
            messages.error(request,"Passwords do not match")
            return redirect('home')


        # Create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your AjTEchLearnS account has been successfully created")
        # return render(request,'success.html')
        return redirect('home')

    else:
        return render(request,'page_404_error.html')