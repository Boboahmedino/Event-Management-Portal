from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Profile, Reservation, Category, Room, Breakout, Catering, Venue
# Create your views here.

def profile(request):
    
    profiles = Profile.objects.filter(customer = request.user)
    # data = Profile.objects.get(pk = 1)
    current_user = request.user
    Full_Name = current_user.username
    Email = current_user.email
    context = {
        'profiles' : profiles,
        'values' :profiles,
        'Full_Name' : Full_Name,
        'Email' : Email, 
      
       
    }

    return render(request, "dashboard/profile.html", context)


    
    
def profile_info(request):
    context = {
        'values' : request.POST
    }
    
    if request.method == 'GET':
        return render(request, "dashboard/profile_info.html")
    
    if request.method == 'POST':
        mobile_number = request.POST['mobile_number']
        address = request.POST['address']
        country = request.POST['country']
        state = request.POST['state']
        
        
        if not mobile_number:
            print('Provide Your Mobile Number')
            messages.warning(request, 'OOPS! Please Provide Your Mobile Number')
            return render(request, "dashboard/profile_info.html", context)
            
        if not address:
            print('Provide Your Contact Address')
            messages.warning(request, 'OOPS! Please Provide Your Contact Address')
            return render(request, "dashboard/profile_info.html", context)
        
        if not country:
            print('Provide Your Country of Residence')
            messages.warning(request, 'OOPS! Please Provide Your Country of Residence')
            return render(request, "dashboard/profile_info.html", context)
        
        if not state:
            print('Provide Your State of Residence')
            messages.warning(request, 'OOPS! Please Provide Your State of Residence')
            return render(request, "dashboard/profile_info.html", context)
         
        Profile.objects.create(customer = request.user, mobile_number = mobile_number, address = address, country = country, state = state )
        print("Your Information has been saved!")
        messages.success(request,'Your Information has been saved!')
        return redirect('profile')


def edit_profile(request, id):
    # pk is an attribute that django set up automatically
    profile = Profile.objects.get(pk = id)
    
    context = {
        
        'profile' : profile,
        'values' : profile,
    }
    
    # to retrieve what was posted the code performs the action
    if request.method == 'GET':
        return render(request, 'dashboard/edit_profile.html', context)
    
    if request.method == 'POST':
        mobile_number = request.POST['mobile_number']
        address = request.POST['address']
        country = request.POST['country']
        state = request.POST['state']
        
        if not mobile_number:
            print('Provide Your Mobile Number')
            messages.warning(request, 'OOPS! Please Provide Your Mobile Number')
            return render(request, "dashboard/edit_profile.html", context)
            
        if not address:
            print('Provide Your Contact Address')
            messages.warning(request, 'OOPS! Please Provide Your Contact Address')
            return render(request, "dashboard/edit_profile.html", context)
        
        if not country:
            print('Provide Your Country of Residence')
            messages.warning(request, 'OOPS! Please Provide Your Country of Residence')
            return render(request, "dashboard/edit_profile.html", context)
        
        if not state:
            print('Provide Your State of Residence')
            messages.warning(request, 'OOPS! Please Provide Your State of Residence')
            return render(request, "dashboard/edit_profile.html", context)
               
        profile.owner =  request.user
        profile.mobile_number = mobile_number
        profile.address = address
        profile.country = country
        profile.state = state
        profile.save()
        print('Profile info updated succesfully')
        messages.success(request, 'Profile Information Updated Successfully')
        return redirect('profile')

def make_reservation(request):
    categories = Category.objects.all()
    rooms = Room.objects.all()
    breakouts = Breakout.objects.all()
    caterings = Catering.objects.all()
    venues = Venue.objects.all()
    
    # prof = get_object_or_404(Profile, pk=id)
 
    context = {
        'categories' : categories,
        'rooms' : rooms,
        'breakouts' : breakouts,
        'caterings' : caterings,
        'venues' : venues,
        'values' : request.POST
    }
    if request.method == 'GET':   
        return render(request, "dashboard/reservation.html", context)
  
    if request.method == 'POST':
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
        
                
        if not event_title:
            print('Event Title is required')
            messages.error(request, 'Event Title is required')     
            return render(request, "dashboard/reservation.html", context)
              
        if not start_date:
            print('Event Start Date is required')
            messages.error(request, 'Event Start Date is required')     
            return render(request, "dashboard/reservation.html", context)
              
              
        if not end_date:
            print('Event End Date is required')
            messages.error(request, 'Event End Date is required')     
            return render(request, "dashboard/reservation.html", context)
              
        if not guest:
            print('Number of Guest is required')
            messages.error(request, 'Number of Guest is required')     
            return render(request, "dashboard/reservation.html", context)
        
        if not time:
            print('Time is required')
            messages.error(request, 'OOPS!Event Time is required')     
            return render(request, "dashboard/reservation.html", context)
        
        
        Reservation.objects.create(customer = request.user, event_title = event_title, category = category, start_date = start_date, end_date = end_date, guest = guest, time = time, room = room, breakout = breakout, catering = catering, venue = venue)
        print('Your info has been saved successfully')
        messages.success(request, "Your request has been submitted successfully, The Lagos State University Event Services will respond on availability within 48 business hours.")  
        return redirect('make_reservation')

def history(request):
    reservations = Reservation.objects.filter(customer = request.user)
    context = {
        'reservations' : reservations,
        'values' :reservations
    }

    return render(request, "dashboard/history.html", context)



from django.contrib.auth.views import PasswordChangeView
from .forms import PasswordChangingForm
from django.urls import reverse_lazy

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('success')


# Successful message after password change
def success(request):
    return render(request, 'dashboard/password_success.html')