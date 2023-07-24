from django.shortcuts import render, redirect
from candidatereg.models import Candidates as c



def result(request):
    candidate= c.objects.all().values()
    context = {'candidate': candidate}
    max = 0
    for i in candidate:
       if i['votes'] > max:
           max = i['votes']
    if request.method == ['POST']:
        return redirect('homepage:home')

    return render(request,'result.html', context)