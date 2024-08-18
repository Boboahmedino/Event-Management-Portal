from django.shortcuts import redirect, render
from authentication.views import login
from django.contrib.auth.decorators import login_required
from .models import Payment
from django.contrib import messages
# Create your views here.


# def pay(request):
#     pays = Payment.objects.all()
#     context ={'pays' : pays
#     }
#     if request.method == 'GET':   
#         return render(request, 'payment/pay.html', context)
#     if request.method == 'POST':
#         pay = request.POST['pay']
        
#         Payment.objects.create(pay = pay)
#         print('Your payment info has been saved successfully')
#         # messages.success(request, "Your request has been submitted successfully, The Lagos State University Event Services will respond on availability within 48 business hours.")  
#         return redirect('select')

def pay(request):
    pays = Payment.objects.all()
    context ={'pays' : pays
    }
    if request.method == 'GET':   
        return render(request, 'payment/pay.html', context)
    if request.method == 'POST':
        pay = request.POST['pay']
        
        Payment.objects.create(pay = pay)
        print('Your payment info has been saved successfully')
        # messages.success(request, "Your request has been submitted successfully, The Lagos State University Event Services will respond on availability within 48 business hours.")  
        return redirect('select')