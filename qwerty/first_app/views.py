from django.shortcuts import render
from django.views import generic
from first_app.models import post

class postlist(generic.ListView):
    queryset = post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class postdetails(generic.DetailView):
    model = post
    template_name = 'post_details.html'
