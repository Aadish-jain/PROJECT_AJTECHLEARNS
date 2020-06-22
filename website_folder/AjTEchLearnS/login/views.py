from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login(request):
    return render(request,'login/login_form.html')

    


def handlelogin(request):
    if request.method == 'POST':
         # Get the post parameters
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = auth.authenticate(username=username1,password=password1)
        if user is not None:
            auth.login(request,user)
            # messages.success(request,"Successfully logged In")
            return redirect('home')
            
        else:
            messages.error(request,"Invalid Credientials")
            return redirect('login')
    else:
        return render(request,'page_404/page_404_error.html')

    #     user = auth.authenticate(username=username1,password=password1)
    #     if user is None:
    #         return render(request,'login_form.html')
    #     else:
    #         return render(request,'success.html')
    # else:
    #     return render(request,'home')

#     if request.method == 'POST':
#         # Get the post parameters
#         loginusername = request.POST['loginusername']
#         loginpassword = request.POST['loginpassword']

        # user = authenticate(username=loginusername,password=loginpassword)
        # if user is not None:
        #     login(request)
        #     # messages.success(request,"Successfully logged In")
        #     return render(request,'index.html')
            
        # else:
        #     # messages.error(request,"Invalid Credientials")
        #     return render(request,'index.html')


#     return render(request,'page_404/page_404_error.html')

