from django.shortcuts import render
from .forms import CustomerForm

def index(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'index.html', {'form': form})
