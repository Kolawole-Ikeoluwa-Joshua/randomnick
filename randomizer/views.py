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


    if request.GET.get('length') and request.GET.get('firstname'):

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

   

    if request.GET.get('secondname'):
        
        f2=open("media/randomizer/docs/db.txt", "r")
        if f2.mode == 'r':
            list_of_secondnames = f2.readlines()

            # print first item in array
            x = random.randint(0, int(240698))
            

            result = list_of_secondnames[x]
            result = result.strip()
        

    if request.GET.get('secondname') and request.GET.get('secondlength'):
        file = open("media/randomizer/docs/db.txt", "r")
        if file.mode == 'r':
            secondnames = file.readlines()
            secondnamesbag = []

            secondlength = int(request.GET.get('secondlength'))
            for secondname in secondnames:
                secondword = secondname.strip()
                if len(secondword) == secondlength:
                    secondnamesbag.append(secondword)
            second_list_length = len(secondnamesbag)
            j = random.randint(0,  second_list_length)
            result = secondnamesbag[j]
    

    if request.GET.get('firstname') and request.GET.get('secondname'):
        f=open("media/randomizer/docs/db.txt", "r")
        if f.mode == 'r':
            list_of_names = f.readlines()

            # print first item in array
            i = random.randint(0, int(240698))
            #result = list_of_names[i]

            result = list_of_names[i]
            result1 = result.strip()

        f2=open("media/randomizer/docs/db.txt", "r")
        if f2.mode == 'r':
            list_of_secondnames = f2.readlines()

            # print first item in array
            x = random.randint(0, int(240698))
            

            result = list_of_secondnames[x]
            result2 = result.strip()
            result = result1+' '+result2

    
    a = request.GET.get('length') and request.GET.get('firstname')
    b = request.GET.get('secondlength') and request.GET.get('secondname')

    if a and b:
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
            result1 = bag[i]

        file = open("media/randomizer/docs/db.txt", "r")
        if file.mode == 'r':
            secondnames = file.readlines()
            secondnamesbag = []

            secondlength = int(request.GET.get('secondlength'))
            for secondname in secondnames:
                secondword = secondname.strip()
                if len(secondword) == secondlength:
                    secondnamesbag.append(secondword)
            second_list_length = len(secondnamesbag)
            j = random.randint(0,  second_list_length)
            result2 = secondnamesbag[j]
            result = result = result1+' '+result2

        



        
    return render(request, 'randomizer/nickname.html', {'name':result})