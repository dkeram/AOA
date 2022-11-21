from django.shortcuts import render, HttpResponseRedirect
from .forms import RegistrationForm
from .models import Phones

# Create your views here.
def home(request):
    phones = Phones.objects.all()
    return render(request,'./html/index.html',{'phones':phones})

def registration(request):
    register_form = RegistrationForm(request.POST)
    if register_form.is_valid():
        register_form.save()
        return HttpResponseRedirect('/phaddress/')
    return render(request, './html/register.html',{'form':register_form})