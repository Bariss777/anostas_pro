from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    return HttpResponse('Hello, world!')

def index(request):
    return HttpResponse('INDEX')


def post_list(request):
    return render(request, 'anostas_app/post_list.html', {})    
