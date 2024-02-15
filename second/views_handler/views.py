from django.shortcuts import render, HttpResponse
from .forms import PersonForm
# Create your views here.

def hello(request):
    #return HttpResponse("Hello World!")
    return render(request, 'hello.html')

def datas(request):
    data = [
        {'Name': 'John', 'Age': 25, 'City': 'New York'},
        {'Name': 'Jane', 'Age': 30, 'City': 'San Francisco'},
        {'Name': 'Bob', 'Age': 22, 'City': 'Chicago'},
    ]
    return render(request, 'datas.html', {'data': data})


def data_input(request):
    entered_data = None

    if request.method == 'POST':
        entered_data = request.POST.get('input_data', None)

    return render(request, 'data_input.html', {'entered_data': entered_data})

def person_form(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'person_form.html', {'form': form, "success": True})
    else:
        form = PersonForm()

    return render(request, 'person_form.html', {'form': form})

