from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages


# Create your views here.

class UsernameValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric caractere'},status=400)
        if User.objects.filter(username=str(username)).exists():
            return JsonResponse({"username_error":"sorry, username already exist"},status=400)
        
        return JsonResponse({'username_valid':True})
    


class emailValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error':'email is invalide'},status=400)
        if User.objects.filter(email=str(email)).exists():
            return JsonResponse({"email_error":"sorry, email is already use"},status=400)
        
        return JsonResponse({'email_valid':True})
    
    
class RegistrationView(View):
    def get(self,request):
        return render(request,"authentication/register.html")
    
    def post(self,request):
        #GET USER DATA
        #VALIDATE
        #CREATE USER ACCOUNT

        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        context = {
            'fieldValues' : request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<8 :
                    messages.error(request,"password too short")
                    return render(request,"authentication/register.html",context)
                
                user = User.objects.create_user(username=username,email=email)
                user.set_password(password)
                user.is_active = False
                user.save()

                messages.success(request, 'Account successfully created')
                return render(request,"authentication/register.html")
    
