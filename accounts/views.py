from django.shortcuts import render,redirect
from accounts.forms import (
	RegistrationForm,
	EditProfileForm
	)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.decorators import 
from django.views.generic import TemplateView
from django.shortcuts import render
#from accounts.forms import ProfileForm
#from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required

# class ProfileView(TemplateView):
# 	template_name='accounts/profile.html'

# 	def get(self,request):
# 		form=ProfileForm()
# 		return render(request, self.template_name,{'form':form})

# Create your views here.

def home(request):
	numbers = [1,2,3,4,5]
	name = 'Milan'

	args = {'myName':name, 'numbers':numbers}
	return render(request,'accounts/home.html')


def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts')
	else:
		form = RegistrationForm()


	args = {'form': form }
	return render(request, 'accounts/reg_form.html',args)

# def logout(request):
# 	auth_logout(request)
# 	return redirect('/')
 	
 	

     
     

@login_required
def view_profile(request):
	args = {'user':request.user}
	return render(request,'accounts/profile.html',args)

@login_required
def edit_profile(request):
	if request.method == "POST":
		form = EditProfileForm(request.POST,instance=request.user)


		if form.is_valid():
			form.save()
			return redirect('/accounts/profile')
		
		

	else:
		form = EditProfileForm(instance=request.user)

	args = {'form':form}
	return render(request,'accounts/edit_profile.html',args)


def change_password(request):
	if request.method == "POST":
		form = PasswordChangeForm(data=request.POST,user=request.user)


		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect('/accounts/profile')
		else:
			return redirect('accounts/change_password')
	
	else:
		form = PasswordChangeForm(user = request.user)

	args = {'form':form}
	return render(request,'accounts/change_password.html',args)


# def edit_userprofile(request):
# 	if request.method == 'POST':
# 		form = UserChangeForm(request.POST)