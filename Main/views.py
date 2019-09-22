from django.shortcuts import render
from django.http import HttpResponse
import time

# (Public) Returns F(n).
def fibonacci(n):
    if n < 0:
        return "No Negative input"
    return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

# Create your views here.
def show(request):
    try:
        data = int(request.POST.get("input"))
    except:
        data = 0
    starttime = time.time() * 1000
    data = fibonacci(data)
    finaltime = time.time() * 1000
    ctime = finaltime - starttime
    context = {"data" : data, "time": ctime}
    return render(request, "Main/index.html", context)
