from unicodedata import category
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import Category, NewsStory
from .forms import StoryForm
from django.db.models import Q
from django.core.exceptions import PermissionDenied


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    
  
    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('search'):
            s_term = self.request.GET.get('search')
            context['all_stories'] = NewsStory.objects.filter(Q(title__icontains=s_term) | Q(author__username=s_term) | Q(author__last_name=s_term) | Q(category__name__iexact=s_term) | Q(content__icontains=s_term)) 
        else:
            context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
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
    fields =  ['image_upload', 'title','content', 'category']
    template_name = 'news/createStory.html'
    

    def form_valid(self, form):
        if form.instance.author == self.request.user:
            return super().form_valid(form)
        return super().form_invalid(form)

    def get_object(self, queryset = None):
        story = super().get_object(queryset)
        if story.author != self.request.user:
            raise PermissionDenied
        return story

    def get_success_url(self):
        story_id = self.object.id
        return reverse('news:story', kwargs={'pk': story_id},)


class StoryDeleteView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deletestory.html'
    success_url = reverse_lazy('news:index')

    def get_object(self, queryset = None):
        story = super().get_object(queryset)
        if story.author != self.request.user:
            raise PermissionDenied
        return story



class CategoryView(generic.DetailView):
    model = Category
    slug_field = 'name'

        
    
     

    
    

