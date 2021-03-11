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
    # generate firstname
    """ position=0
    flag=False"""
    length = int(request.GET.get('length',6))
    if request.GET.get('firstname'):
        f=open("media/randomizer/docs/db.txt", "r")
        if f.mode == 'r':
            list_of_names = f.readlines()


            # print first item in array
            i = random.randint(0, int(240698))
            #result = list_of_names[i]

        

            
            result = list_of_names[i]

            letters =''
            letters += result
            letters = letters.strip()
            count = len(list(letters))
            if  count == length:
                return render(request, 'randomizer/nickname.html', {'result':result})
     

    print(count)
    print (letters)
    
    return render(request, 'randomizer/nickname.html', {'names':letters, 'count':count})


    
    
    
    

    
        


