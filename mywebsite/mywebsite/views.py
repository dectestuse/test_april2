from django.http import HttpResponse

def home(request):
    return HttpResponse("Hii Welcome to the my world")