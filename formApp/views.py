from django.shortcuts import render
from .forms import registrationForm
# Create your views here.

def registerPage(request):
    form=registrationForm(request.POST or None)
    context = {'form': form}
    if request.method=="POST":
        if form.is_valid():
            form=form.cleaned_data
            context={'value':form}
            print('the first Name Is: ',form['firstName'] )
            print('the last Name Is: ',form['lastName'] )
            print('the password Is: ',form['password'] )
    return render(request, 'register.html', context)