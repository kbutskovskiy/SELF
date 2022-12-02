from django.shortcuts import render
from django.http import HttpResponse
import math
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import mpld3

def voltage(array, a, c, tim):
    t = 0
    for i in range(100):
        array.append(c * a * math.sin(100 * t - math.pi / 2))
        tim.append(t)
        t = t + 0.1


someArray = []
tim = []
voltage(someArray, 100, 10e-6, tim)

plt.plot(tim, someArray)

plt.title("Line graph")
plt.ylabel('Y axis')
plt.xlabel('X axis')
fig = Figure(figsize=(10,10))
plt.savefig('bank_data.png')

def index(request):
    return render(request, 'main/index.html')

html_str = mpld3.fig_to_html(fig)
Html_file = open("index.html","w")
Html_file.write(html_str)
Html_file.close()
def about(request):
    return render(request, 'main/about.html')
