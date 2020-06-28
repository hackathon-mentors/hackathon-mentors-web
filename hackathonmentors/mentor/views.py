from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from hackathonmentors.views import HackathonMentorsMixin
from mentor.models import Mentor
from user.models import CustomUser as User


class MentorListView(HackathonMentorsMixin, ListView):
    model = Mentor
    context_object_name = 'mentors'
    paginate_by = 25  # NOTE: TBD
    template_name = "mentor/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MentorDetailsView(HackathonMentorsMixin, DetailView):
    model = Mentor
    template_name = "mentor/view.html"
    context_object_name = 'mentor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        user = User.objects.filter(username=slug)
        if user:
            user = user.first()
            mentor = Mentor.objects.filter(user_id=user.id)
            print(mentor)
        
        return mentor
