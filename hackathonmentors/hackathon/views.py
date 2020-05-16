from django.shortcuts import render

from hackathonmentors.views import BaseView
from hackathon.models import Hackathon

class HackathonListView(BaseView):
    model = Hackathon
    paginate_by = 25  # NOTE: TBD
    template_name = "hackathon/index.html"
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
