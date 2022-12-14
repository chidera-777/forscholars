from django.urls import path
from . import views


urlpatterns=[
	path('profile/', views.profile, name="profile" ),
	path('register/', views.registrationView, name="register" ),
	path('login/', views.loginView, name="login" ),
	path('logout/', views.logoutView_1, name="logout_1" ),
	path('logout_2/', views.logoutView, name="logout_2" ),
	path('update-profile/', views.profileUpdate, name='update-profile')
]