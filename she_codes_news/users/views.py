from django.urls import reverse_lazy
from django.views.generic.edit import CreateView 
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomerUserChangeForm




class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'


class UserProfile(generic.DetailView):
    model =CustomUser
    template_name = 'users/userProfile.html'
    context_object_name = 'profile'

class UpdateUserView(generic.UpdateView):   
    form_class = CustomerUserChangeForm
    model =CustomUser
    context_object_name = 'userForm'
    template_name = 'users/updateUser.html'

    def get_object(self, queryset = None):
        return self.request.user

    
    
    

 
