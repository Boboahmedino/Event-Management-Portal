from django.shortcuts import redirect, render
from authentication.views import login
from django.contrib.auth.decorators import login_required
from .models import Booking, Category, Room, Breakout, Catering, Venue
from django.contrib import messages
from django.http import HttpResponse

# from django.contrib.auth.models import User, auth
# from  authentication.models import Customer



# Create your views here.


# @login_required(login_url='authentication/login')
def select(request):
    return render(request,'booking/select.html')


    
def contact(request):
    categories = Category.objects.all()
    rooms = Room.objects.all()
    breakouts = Breakout.objects.all()
    caterings = Catering.objects.all()
    venues = Venue.objects.all()
    
    context = {
        'categories' : categories,
        'rooms' : rooms,
        'breakouts' : breakouts,
        'caterings' : caterings,
        'venues' : venues,
        'values' : request.POST
        # values allows user to see previous typed commands
    }
    if request.method == 'GET':   
        return render(request, 'booking/contact_info.html', context)
  
      
  

      
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        contact_address = request.POST['contact_address']
        event_title = request.POST['event_title']
        category =request.POST['category']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        guest = request.POST['guest']
        time = request.POST['time']
        room = request.POST['room']
        breakout = request.POST['breakout']
        catering = request.POST['catering']
        venue = request.POST['venue']
        
        
        if not first_name:
            print('First Name is required')
            messages.error(request, 'First Name is required')     
            return render(request, 'booking/contact_info.html', context)
               
        if not last_name:
            print('Last Name is required')
            messages.error(request, 'Last Name is required')     
            return render(request, 'booking/contact_info.html', context)
        
        if not email:
            print('Email is required')
            messages.error(request, 'Email is required')     
            return render(request, 'booking/contact_info.html', context)
        
        if not mobile_number:
            print('Mobile Number is required')
            messages.error(request, 'Mobile Number is required')     
            return render(request, 'booking/contact_info.html', context)
        
        if not contact_address:
            print('Contact Address is required')
            messages.error(request, 'Contact Address is required')     
            return render(request, 'booking/contact_info.html', context)
        
        if not event_title:
            print('Event Title is required')
            messages.error(request, 'Event Title is required')     
            return render(request, 'booking/contact_info.html', context)
              
        if not start_date:
            print('Event Start Date is required')
            messages.error(request, 'Event Start Date is required')     
            return render(request, 'booking/contact_info.html', context)
              
              
        if not end_date:
            print('Event End Date is required')
            messages.error(request, 'Event End Date is required')     
            return render(request, 'booking/contact_info.html', context)
              
        if not guest:
            print('Number of Guest is required')
            messages.error(request, 'Number of Guest is required')     
            return render(request, 'booking/contact_info.html', context)
        
        if not time:
            print('Time is required')
            messages.error(request, 'Time is required')     
            return render(request, 'booking/contact_info.html', context)
        
       
        # Save all users input
        
        Booking.objects.create(first_name = first_name, last_name = last_name, email = email, mobile_number = mobile_number,contact_address = contact_address, event_title = event_title, category = category, start_date = start_date,end_date = end_date,
                               guest = guest, time = time, room = room, breakout = breakout, catering = catering, venue = venue)
        print('Your info has been saved successfully')
        messages.success(request, "Your request has been submitted successfully, The Lagos State University Event Services will respond on availability within 48 business hours.")  
        # return redirect('select')
  
        return render(request, 'booking/info.html', context)
    
        # return redirect('pay')
    
        # return render(request, 'booking/contact_info.html')



