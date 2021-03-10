from django.shortcuts import render
# import random
import random



# Create your views here.
# views handle requests and redirects web pages
def home(request):
    return render(request, 'randomizer/home.html')

def nickname(request):
    
    # added read feature to parse db.txt
    #nicknames = f.read()

    if request.GET.get('firstname'):
        f=open("media/randomizer/docs/db.txt", "r")
        if f.mode == 'r':
            list_of_names = f.readlines()
            # print first item in array
            

    
            i = random.randint(0, int(240698))
            
            result = list_of_names[i]

            


    return render(request, 'randomizer/nickname.html', {'names':result})
        

    



    
   