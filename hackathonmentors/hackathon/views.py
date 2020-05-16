from django.shortcuts import render

from hackathonmentors.views import HackathonMentorsMixin
from hackathon.models import Hackathon


class HackathonListView(HackathonMentorsMixin, ListView):
    model = Hackathon
    context_object_name = 'hackathons'
    paginate_by = 25  # NOTE: TBD
    template_name = "hackathon/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
