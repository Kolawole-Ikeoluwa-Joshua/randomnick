from django.shortcuts import render
# import random
import random



# Create your views here.
# views handle requests and redirects web pages
def home(request):
    return render(request, 'randomizer/home.html')

def nickname(request):
    
    f=open("media/randomizer/docs/db.txt", "r")
    if f.mode == 'r':
        nicknames = f.read()
        print(nicknames)





    
    return render(request, 'randomizer/nickname.html', {'names':nicknames})