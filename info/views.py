from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def homeview(request):
    return render(request, 'info/home.html')


def contactview(request):
    if request.method =="POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Thank you, {form.instance.full_name} your form has submitted successfully. We will reach out to you shortly.')
            return redirect('info:contact')
    cform = ContactForm
    context ={
        'form':cform
        }
    return render(request, 'info/contact.html',context)



def noticeview(request):
    return render(request, 'info/notice.html')