from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def order(request):
    return render(request,'order_page.html')
