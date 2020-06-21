from django.shortcuts import render,redirect
from . models import Contact
from django.contrib import messages
from . import urls
# Create your views here.
def contact(request):
    # messages.success(request,'Welcome to contact')
    return render(request,'contact.html')
def contact_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<2:
            messages.error(request,"Please fill the form correctly")
            return redirect('/contact/')
        else:
            contact = Contact(name = name, email = email, phone=phone, content=content)
            contact.save()
            messages.success(request,'We will Contact and resolve your issue within 24 hours..')
    return redirect('/')