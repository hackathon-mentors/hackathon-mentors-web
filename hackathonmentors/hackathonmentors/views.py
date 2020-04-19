from django.shortcuts import render

from django.views.generic.base import TemplateView


class HackathonMentorsMixin(object):
    pass


class BaseView(HackathonMentorsMixin, TemplateView):
    pass
