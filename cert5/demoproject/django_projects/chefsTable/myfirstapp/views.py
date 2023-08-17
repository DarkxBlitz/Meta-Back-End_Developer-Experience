from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from myfirstapp.forms import LogForm

def hello(request):
    return HttpResponse("hello, world. Making my first django app here :D")

def homepage(request):
    return HttpResponse("Welcome to my website!")

def menu(request):
    html_path = "C:\my_hobby_projects\meta_certificate _folder\Meta-Back-End_Developer-Experience\cert5\demoproject\django_projects\chefsTable\myfirstapp\lemon_website\src\index.html"
    menu_html_file = open(html_path, "r")
    return HttpResponse(menu_html_file)

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)

    




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