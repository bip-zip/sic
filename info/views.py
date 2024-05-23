from django.shortcuts import render

def homeview(request):
    return render(request, 'home.html')

def contactview(request):
    return render(request, 'contact.html')

def noticeview(request):
    return render(request, 'notice.html')