from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from myfirstapp.forms import LogForm

def hello(request):
    return HttpResponse("hello, world. Making my first django app here :D")

def homepage(request):
    return HttpResponse("Welcome to my website!")

def menu(request):
    return render(request, 'partials/index.html')

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "partials/home.html", context)

def menu2(request):
    menuitem = {'main_course' : [
        {'name' : 'Greek Salad', 'price': '12'},
        {'name': 'pizza', 'price': '4'},
        {'name': 'gyro', 'price': '10'},
                                 
    ]}
    return render(request, 'partials/menu.html', menuitem)




    ''' EXAMPLE OF GET AND POST methods in the home(request) function
def myview(request): 
    if request.method=='GET': 
        val = request.GET['key'] 
        #perform read or delete operation on the model 
    if request.method=='POST': 
        val = request.POST['key'] 
        #perform insert or update operation on the model 

'''

'''RENDERING TEMPLATE : Django view loads the template web page, inserts certain context data at the placeholders marked with tags, and returns it as the response
def myview(request):  

      if request.method=='GET':  
            #perform read or delete operation on the model  

      if request.method=='POST':  
            #perform insert or update operation on the model  
            context={ } #dict containing data to be sent to the client  

      return render(request, 'mytemplate.html', context) 
      '''
'''CLASS based views
from django.views import View 
class MyView(View): 
    def get(self, request): 
        # logic to process GET request
        return HttpResponse('response to GET request') 
 
    def post(self, request): 
        # <logic to process POST request> 
        return HttpResponse('response to POST request') 
'''
#known as the view function, takes an  http request object as its first parameter "request"
#Ex: content = <html><body><h1>Welcome to my website</h1></body></html>
#Excontinued: return HTTPResponse(content)