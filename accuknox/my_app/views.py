from django.shortcuts import render
from django.contrib.auth.models import User
import time

def create_user(request):
    start = time.time()
    user = User.objects.create(username='test_user')
    end = time.time()
    total_time = end - start
    return render(request, 'core/index.html', {'time': total_time})
