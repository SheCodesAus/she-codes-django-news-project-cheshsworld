from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from news.models import NewsStory



class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'


class UserProfile(generic.DetailView):
    model =CustomUser
    template_name = 'users/userProfile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_story'] = NewsStory.objects.filter(author=self.kwargs['pk'])
        print(context['user_story'])
        return context
