from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from links.forms import LinkForm


# Create your views here.
def home(request):
    return render(request, 'index.html')


@login_required()
def add_link_popup(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        link = form.save(commit=False)
        link.user = User.objects.get(pk=1)
        link.save()
    else:
        form = LinkForm()
    return render(request, 'add_link_popup.html', {"form": form})