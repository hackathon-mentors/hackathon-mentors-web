from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

from hackathonmentors.views import HackathonMentorsMixin
from mentor.models import Mentor
# Create your views here.


class MentorListView(HackathonMentorsMixin, ListView):
    model = Mentor
    context_object_name = 'mentors'
    paginate_by = 25  # NOTE: TBD
    template_name = "mentor/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MentorDetailView(HackathonMentorsMixin, DetailView):
    model = Mentor
    template_name = "mentor/view.html"
    context_object_name = 'mentor'
