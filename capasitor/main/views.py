from django.shortcuts import render, redirect
from django.http import HttpResponse
import math
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from django.shortcuts import render

from .forms import ValueForm


def voltage(capacityArray, volt, capacity, timeArray, frequency, workTime):
    t = 0
    for t in range(workTime):
        capacityArray.append(capacity * volt * math.sin(frequency * t - math.pi / 2))
        timeArray.append(t)
        t = t + 0.1


def resist(array, volt, frequency, workTime):
    t = 0
    while t != 10:
        array.append(volt * math.sin(frequency * t))
        t = t + 0.1

capacity = 0
resistance = 0
frequency = 0
time = 0
volta = 0

def index(request):
    error = ''
    if request.method == 'POST':
        form = ValueForm(request.POST)
        global capacity
        global resistance
        global frequency
        global time
        global volta
        capacity = int(form['capacity'].value())
        resistance = int(form['resistance'].value())
        frequency = int(form['frequency'].value())
        time = int(form['time'].value())
        volta = int(form['amplitude'].value())
        capacityArray = []
        timeArray =[]
        voltage(capacityArray, volta, capacity, timeArray, frequency, time)
        plt.plot(timeArray, capacityArray)
        plt.title("На конденсаторе")
        plt.ylabel('Voltage')
        plt.xlabel('Time')
        fig1 = Figure(figsize=(10, 10))
        plt.savefig('voltageOnCapacitor.png')
        plt.close(fig1)
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
