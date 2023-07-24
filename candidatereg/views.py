from django.shortcuts import render, redirect
from .forms import CandidatesForm

from voter.models import VoterList
# Create your views here.


def register(request):
    form=CandidatesForm()
    if request.method == "POST":
        form=CandidatesForm(request.POST,request.FILES)
        #print(form.is_valid())
        #print(request.POST)
        #print(request.FILES)
        #print(form)
        if form.is_valid():
            form.save()
        return redirect('homepage:home')
    template='candidatereg/registration.html'
    data={'form':form, 'voter':VoterList.objects.all().values()}
    return render(request,template,data)

