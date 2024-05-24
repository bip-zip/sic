from django.shortcuts import render

def courseview(request):
    return render(request, 'lms/courses.html')