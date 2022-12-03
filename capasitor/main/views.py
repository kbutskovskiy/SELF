from django.shortcuts import render, redirect
from django.http import HttpResponse
import math
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import mpld3
from .models import Value
from .forms import ValueForm


def voltage(array, a, c, tim):
    t = 0
    for i in range(100):
        array.append(c * a * math.sin(100 * t - math.pi / 2))
        tim.append(t)
        t = t + 0.1


def resist(array, a):
    t = 0
    for i in range(100):
        array.append(a * math.sin(100 * t))
        t = t + 0.1


capacityArray = []
resistArray = []
tim = []
voltage(capacityArray, 100, 10e-6, tim)
resist(resistArray, 100)

plt.plot(tim, capacityArray)

plt.title("На конденсаторе")
plt.ylabel('Voltage')
plt.xlabel('Time')
fig1 = Figure(figsize=(10, 10))
plt.savefig('voltageOnCapacitor.png')
plt.close(fig1)

plt.plot(tim, resistArray)

plt.title("На резисторе")
plt.ylabel('Voltage')
plt.xlabel('Time')
fig2 = Figure(figsize=(10, 10))
plt.savefig('voltageOnResistor.png')


def index(request):
    error = ''
    if request.method == 'POST':
        form = ValueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'неверная форма'
    form = ValueForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/index.html', data)
