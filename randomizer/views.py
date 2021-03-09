from django.shortcuts import render


# Create your views here.
# views handle requests and redirects web pages
def home(request):
    return render(request, 'randomizer/home.html')

def nickname(request):
    return render(request, 'randomizer/nickname.html')