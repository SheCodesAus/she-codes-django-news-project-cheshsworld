from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import NewsStory
from .forms import StoryForm
from django.db.models import Q


class IndexView(generic.ListView):
    template_name = 'news/index.html'
  
    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        if self.request.GET.get('search'):
            s_term = self.request.GET.get('search')
            context['all_stories'] = NewsStory.objects.filter(Q(title__icontains=s_term) | Q(author__username=s_term) | Q(author__last_name=s_term))
        else:
            context['all_stories'] = NewsStory.objects.all()
        return context


class StoryView(generic.DetailView):
    model =NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
    
  

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StoryUpdateView(generic.UpdateView):
    model = NewsStory
    fields = ['title','content','image_upload']
    template_name = 'news/createStory.html'
    

    def form_valid(self, form):
        if form.instance.author == self.request.user:
            return super().form_valid(form)
        return super().form_invalid(form)

    def get_success_url(self):
        story_id = self.object.id
        return reverse('news:story', kwargs={'pk': story_id},)




class StoryDeleteView(generic.DeleteView):
    model = NewsStory
    success_url = reverse_lazy()
    

  

    
    

