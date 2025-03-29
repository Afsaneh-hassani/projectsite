from django.shortcuts import render, redirect
from website.models import Contact
from website.forms import  ContactForm
from django.contrib import messages

# Create your views here.


def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message submitted successfully!')
            return redirect('website:contact')
        else:
            
            print("Form errors:", form.errors)
            messages.error(request, 'Please fix the following errors:')
    else:
        form = ContactForm()
    
    return render(request, 'website/contact.html', {'form': form})