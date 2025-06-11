from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author' : 'Rahim', 'age' :  5, 'lst' : ['python','is','best'],
         'birthday' : datetime.datetime.now(),'courses' : [
             {
                 'id' : 1,
                 'name': 'Python',
                 'fee' : 500
             },
             {
                 'id' : 2,
                 'name' : 'Django',
                 'fee' : 10000
             },
             {
                 'id' : 3,
                 'name' : 'C',
                 'fee' : 2000
             },
     ]}
    return render(request, 'home.html', d)