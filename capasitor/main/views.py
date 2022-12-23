from django.shortcuts import render, redirect
from django.http import HttpResponse
import math
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from django.shortcuts import render

from .forms import ValueForm


def impulse(impulseArray, volt, timeArray, workTime, duration):
    t = 0
    while t < workTime:
        if (t // duration) % 2 == 0:
            impulseArray.append(volt)
            timeArray.append(t)
        else:
            impulseArray.append(0)
            timeArray.append(t)
        t = t + 0.05


def voltage(capacityArray, volt, capacity, timeArray, workTime, resistance, duration):
    t = 0
    while t < workTime:
        if (t // duration) % duration == 0:
            capacityArray.append(volt * (1 - math.pow(math.e, -t / (resistance * capacity))))
            timeArray.append(t)
        else:
            capacityArray.append(volt * math.pow(math.e, -t / (capacity * resistance)))
            timeArray.append(t)
        t = t + 0.1


def resist(array, volt, workTime, timeArray, resistance, duration):
    t = 0
    while t < workTime:
        if (t // duration) % duration == 0:
            array.append(volt * math.pow(math.e, -t / (capacity * resistance)))
            timeArray.append(t)
        else:
            array.append(volt * (1 - math.pow(math.e, -t / (resistance * capacity))))
            timeArray.append(t)
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
        capacity = float(form['capacity'].value())
        volta = float(form['amplitude'].value())
        duration = float(form['duration'].value())
        resistance = float(form['resistance'].value())
        time = float(form['time'].value())
        capacityArray = []
        resistArray = []
        impulseArray = []
        timeArray1 = []
        timeArray2 = []
        timeArray3 = []
        voltage(capacityArray, volta, capacity, timeArray1, time, resistance, duration)
        resist(resistArray, volta, time, timeArray2, resistance, duration)
        impulse(impulseArray, volta, timeArray3, time, duration)

        plt.plot(timeArray3, impulseArray)
        plt.title("Напряжение источника")
        plt.ylabel('Напряжение, В')
        plt.xlabel('Время, с')
        plt.grid(True)
        fig3 = Figure()
        plt.savefig('Impulse.png')
        plt.close(fig3)
        plt.cla()
        plt.clf()

        plt.plot(timeArray1, capacityArray)
        plt.title("Напряжение на конденсаторе")
        plt.ylabel('Напряжение, В')
        plt.xlabel('Время, с')
        plt.grid(True)
        fig1 = Figure(figsize=(10, 10))
        plt.savefig('voltageOnCapacitor.png')
        plt.close(fig1)
        plt.cla()
        plt.clf()

        plt.plot(timeArray2, resistArray)
        plt.title("Напряжение на резисторе")
        plt.ylabel('Напряжение, В')
        plt.xlabel('Время, с')
        plt.grid(True)
        fig2 = Figure(figsize=(10, 10))
        plt.savefig('Resist.png')
        plt.close(fig2)
        plt.cla()
        plt.clf()
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
