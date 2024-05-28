from django.shortcuts import render
from .forms import ContactForm

def homeview(request):
    return render(request, 'info/home.html')


def contactview(request):
    if request.method =="POST":
        form = ContactForm(request.POST)
        print('POST METHOD CALLED')  
        print(form.data)
    
        
    cform = ContactForm
    context ={
        'form':cform
        }
    return render(request, 'info/contact.html',context)



def noticeview(request):
    return render(request, 'info/notice.html')