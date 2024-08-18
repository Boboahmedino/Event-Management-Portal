from email import message
from genericpath import exists
from django import conf, views
from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.mail import EmailMessage

# from .models import Customer

# Create your views here.



# Main registration Page for a user 
 




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        
        # # this keeps values in the field, then attach ',context' to any redirected page
        # context = {
        #     'fieldvalues' : request.POST
        # }
        
        if password == confirm_password:
            # if User.objects.filter(username = username).exists():
            #     # this prints in my terminal the message if the username already exist
            #     print('Username has been used')
            #     # i thought since the user can not see my terminal i used messages info to print to the use on the web page
            #     messages.warning(request, 'Username has been used')
            #     return redirect('register')
            
            if User.objects.filter(email = email).exists():
                print ('Email has been used')
                messages.warning(request, 'Email has been used')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.set_password(password)
                # user.is_active = True
                user.save()
                
                # for the user to recieve email for authentication
                # email_subject   = 'Lagos State University Event Services'
                # email_body = '''Event Services in Lagos State University oversees the operations of different major events,
                #                 including outdoor events on campus. Event Services operations involves the responsibility of creating beautiful events,
                #                 from concept to the completion of the event, Event Services will aid reservation, planning, 
                #                 Event security and Production elements to make your event pleasurable as you imagined it.
                #             '''
                # email = EmailMessage(
                #     email_subject,
                #     email_body,
                #     'email address',
                #     [email]
                # )
                # email.send(fail_silently=False)
                
                print('User account created')
                messages.success(request, 'Account created successfully, Login')
                return render(request, 'authentication/login.html') 
                # return redirect ('profile_creation')
                           
                # return redirect('login')
            
        elif len(password) < 6:
            print('Password too short')       
            messages.error(request, 'Password too short, It should be 6 or more characters')
            return redirect('register')   
        else:
            print("Password doesn't match")   
            messages.error(request, "Password doesn't match")   
            return redirect('register')
    else:
        return render(request, 'authentication/register.html')
    



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # auth verifies the user's account in the database by taking request
        user = auth.authenticate(username = User.objects.get(email = username), password = password)
        
        # user = auth.authenticate(username = username, password = password)

        # if user has an account
        if user is not None:
            auth.login(request, user)
            print(f'Welcome {user} you are now logged in')
            messages.success(request, f'Welcome {user} you are now logged in')
            return render(request, 'dashboard/dash.html')
        
            
        else:
            print('Your e-mail or password is incorrect, Please fill all fields correctly')
            messages.error(request, 'Your e-mail or password is incorrect,  fill all fields correctly')
            # messages.error(request, '')
            return redirect('login')

    else:
        return render(request, 'authentication/login.html')  


def logout(request):
    auth.logout(request)
    print("You have been logged out")
    messages.success(request, "You have been logged out")
    return redirect('login')
       












# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         mobile_number = request.POST['mobile_number']
#         address = request.POST['address']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
        
        
#         if password == confirm_password:          
#             if Customer.objects.filter(email = email).exists():
#                 print ('Email has been used')
#                 messages.warning(request, 'Email has been used')
#                 return redirect('register')
            
#             else:
#                 user = Customer(username = username, email = email, mobile_number = mobile_number, address = address, password = password)
#                 user.save()
                          
#                 print('User account created')
#                 messages.success(request, 'Welcome! Account created successfully')
#                 return render(request, 'booking/select.html')
             
            
#         elif len(password) < 6:
#             print('Password too short')       
#             messages.error(request, 'Password too short, It should be 6 or more characters')
#             return redirect('register')   
#         else:
#             print("Password doesn't match")   
#             messages.error(request, "Password doesn't match")   
#             return redirect('register')
#     else:
#         return render(request, 'authentication/register.html')
        

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
               
#         # this allows me use email as usaername to login
#         user =  Customer.objects.filter( username = Customer.objects.get(email = username), password = password)
        
#         if user is not None:
#             print(f'Welcome Back! {username}')
#             messages.success(request, f'Welcome Back! {username}')
#             return render(request, 'booking/select.html')
            
            
#         else:
#             print('Your email or password is incorrect, Please fill all fields correctly')
#             messages.error(request, 'Your email or password is incorrect,  fill all fields correctly')
#             return redirect('login')          
#     else:
#         return render(request, 'authentication/login.html')  

# class LogoutView(View):
#     def post(self,request):
#         auth.logout(request)
#         print("You have been logged out")
#         messages.success(request, "You have been logged out")
#         return redirect('login') 
