from django.conf.urls import url
from . import views
from django.contrib.auth.views import (login,logout,password_reset,password_reset_done,password_reset_confirm,
	password_reset_complete
	)
#from accounts.views import ProfileView
app_name='accounts'
urlpatterns=[
		 url(r'^$',views.home),

		 url(r'^login/$',login,{'template_name': 'accounts/login.html'}), 
		 url(r'^logout/$',logout,{'template_name': 'accounts/logout.html'}), 
		 url(r'^register/$' ,views.register,name='register'),
		 url(r'^profile/$' ,views.view_profile,name = 'view_profile'),
		# url(r'^profile/$' ,ProfileView.as_view(),name = 'ProfileView'),
		 url(r'^profile/edit/$',views.edit_profile,name= 'edit_profile'),
		 url(r'^change-password/$',views.change_password,name='change_password'),
		 url(r'^reset-password/$',password_reset,{'template_name':'accounts/reset_password.html','post_reset_redirect':'accounts:password_reset_done','email_template_name':'accounts/reset_password_email.html'},name='reset-password'),
		 url(r'^reset-password/done/$',password_reset_done,{'template_name':'accounts/reset_password_done.html'},name='password_reset_done'),
		 url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
		 password_reset_confirm,{'post_reset_redirect':'accounts:password_reset_complete'}, name='password_reset_confirm'),
		 url(r'^reset-password/complete/$',password_reset_complete,name='password_reset_complete')


	]

	