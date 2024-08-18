from django.urls import path
from .import views
# for password change
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView

urlpatterns = [
    path('profile', views.profile, name = 'profile'),  
    path('edit_profile<int:id>', views.edit_profile, name = 'edit_profile'),  
    path('profile_info', views.profile_info, name = 'profile_info'),
    path('make_reservation', views.make_reservation, name = 'make_reservation'),
    path('history', views.history, name = 'history' ),
    # path('change_password', auth_views.PasswordChangeView.as_view(template_name ='dashboard/password.html' )),
    path('change_password', PasswordsChangeView.as_view(template_name ='dashboard/password.html' ), name = 'change_password'),
    path('success', views.success, name = 'success' ),
    ]
