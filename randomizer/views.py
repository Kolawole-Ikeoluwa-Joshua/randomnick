from django.shortcuts import render
# import random
import random
from random import randint



# Create your views here.
# views handle requests and redirects web pages
def home(request):
    return render(request, 'randomizer/home.html')

def nickname(request):
    if request.GET.get('firstname'):
        
        f=open("media/randomizer/docs/db.txt", "r")
        if f.mode == 'r':
            list_of_names = f.readlines()

            # print first item in array
            i = random.randint(0, int(240698))
            #result = list_of_names[i]

            result = list_of_names[i]
            result = result.strip()

    if request.GET.get('length'):

        f=open("media/randomizer/docs/db.txt", "r")
        if f.mode == 'r':
            list_of_names = f.readlines()
            bag = []


            length = int(request.GET.get('length'))
            for name in list_of_names:
                word = name.strip()
                if len(word) == length:
                    bag.append(word)
                    
                    #print(first_word)
            random_length = len(bag)
            i = random.randint(0, random_length)
            result = bag[i]

    return render(request, 'randomizer/nickname.html', {'names':result})
