from django.shortcuts import render

def homeview(request):
    return render(request, 'info/home.html')

def contactview(request):
    return render(request, 'info/contact.html')

def noticeview(request):
    return render(request, 'info/notice.html')