from django.shortcuts import render, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):

    if 'data' not in request.session:
        request.session['data'] = []

    return render(request, 'words/index.html')

def process(request):


    if 'big' not in request.POST:
        size = 'off'
    else:
        size = request.POST['big']


    data = {
        'thing': request.POST['word'],
        'color': request.POST['color'],
        'big': size,
        'time': strftime('%Y-%m-%d %H:%M %p', gmtime()),
    }
    
    session_data = request.session['data']
    session_data.append(data)
    request.session['data'] = session_data
    print request.session['data']
    return redirect('/')

def reset(request):

    request.session.clear()

    return redirect('/')
