from django.shortcuts import render
from datetime import datetime

def new_year(request):
    now = datetime.now()

    return render(request, "newyear/index.html",{
        "newyear": now.month == 1 and now.day == 1
    })