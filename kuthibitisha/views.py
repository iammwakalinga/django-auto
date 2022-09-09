from contextlib import redirect_stderr
from email import header, message
from multiprocessing import context


from .info import MessHandler
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
import random
from django.contrib.auth import login






def login(request):
    if request.method =='POST':
       phone_number=request.POST.get('phone_number') 
       profile=Profile.objects.filter(phone_number=phone_number)
       if not profile.exists():
            return redirect('/register/')
       profile[0].otp =random.randint(1000,9999)
       profile[0].save()
       message_handler=MessHandler(phone_number,profile[0].otp ).send_otp_on_phone()
       return redirect(f'/otp/{profile[0].uid}')

    return render(request,'login.html')

def register(request):
    if request.method =='POST':
        username=request.POST.get('username')
        phone_number=request.POST.get('phone_number')
        user=User.objects.create(username=username)
        user.save()
        profile= Profile.objects.create(user=user,phone_number=phone_number)
        profile.save()
        return redirect(request,'/')
    
    
    
    return render(request,'register.html')




def cart(request):
    return render(request,'cart.html')
      
def otp(request,uid):
    
    
    
    if request.method=='POST':
        otp=request.POST.get('otp')
        profile=Profile.objects.get(uid=uid)

        if otp==profile.otp:
            login(profile.user,request)
            return redirect('cart')
        
            
        return redirect('/otp/{uid}')
       
    return render(request,'otp.html')
    


