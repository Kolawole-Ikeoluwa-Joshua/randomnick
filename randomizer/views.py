from django.shortcuts import render
# import random
import random
import csv


# Create your views here.
# views handle requests and redirects web pages
def home(request):
    return render(request, 'randomizer/home.html')

def nickname(request):
    # get a list of names from name csv file
    
    with open('media/randomizer/docs/name_file.csv', newline='') as File:  
         nameList = list(csv.reader(File))


    
    return render(request, 'randomizer/nickname.html', {'names':nameList})