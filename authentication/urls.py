from .views import RegistrationView, UsernameValidationView, emailValidationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register',RegistrationView.as_view(),name='register'),
    path('validate-username',csrf_exempt(UsernameValidationView.as_view()),name="username_validation"),
    path('validate-email',csrf_exempt(emailValidationView.as_view()),name="email_validation")
]
