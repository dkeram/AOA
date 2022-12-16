from django.shortcuts import render, HttpResponseRedirect, HttpResponse,redirect
from django.template import loader
from .forms import RegistrationForm
from .models import Phones

# Home Page all contacts from table are visible
def phaddress_home(request):
    phones = Phones.objects.all()
    return render(request,'./html/index.html',{'phones':phones})


# Create a New Contact
def phaddress_registration(request):
    register_form = RegistrationForm(request.POST)
    if register_form.is_valid():
        register_form.save()
        return HttpResponseRedirect('/phaddress/')
    return render(request, './html/register.html',{'form':register_form})

# Delete an existing Contact
def phaddress_delete(request,contact_id):
    contact = Phones.objects.get(pk=contact_id)
    contact.delete()
    return redirect('/phaddress/')

# Edit an existing Contact
def phaddress_edit(request,contact_id):
    contact=Phones.objects.get(pk=contact_id)
    edit_form=RegistrationForm(request.POST or None, instance=contact)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('/phaddress/')
    return render(request,'./html/update_contact.html',{'contact':contact,'form':edit_form}) 