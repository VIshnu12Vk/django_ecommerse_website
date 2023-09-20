from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login,logout,authenticate
from .forms import UserCreateForm
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.shortcuts import redirect
from User_Profile_App.models import User_Info
from django.contrib.auth.decorators import login_required

# user signaccount
def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html',
                       {'form':UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('products')
            except IntegrityError:

                return render(request,'signupaccount.html',{'form':UserCreateForm,'error':'Username already taken. Choosenew username.'})
        else:
            return render(request, 'signupaccount.html',{'form':UserCreateForm,'error':'Passwords do not match'})
        
# user logout  
@login_required  
def logoutaccount(request):        
    logout(request)
    return redirect('products')

# user login
def loginaccount(request):    
    if request.method == 'GET':
        return render(request, 'login_form.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request,
          username=request.POST['username'],
          password=request.POST['password'])  
        if user is None:
            return render(request,'login_form.html',{'form': AuthenticationForm(),'error': 'username and password donot match'})
        else:
            login(request,user)
            return redirect('products')
        
# user account detailes
@login_required
def account_user(request):
    user_id = request.user.id
    user_details=get_object_or_404(User_Info, user_name=user_id)
    context = {'user':user_details}
    return render(request,"account_details.html",context)