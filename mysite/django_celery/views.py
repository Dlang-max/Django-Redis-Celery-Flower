from django.shortcuts import render
from .tasks import celery_worker_test
from django.views.decorators.csrf import csrf_exempt
from .froms import TestForm


# Create your views here.
def view(request):

    if request.method == "POST":
        task = celery_worker_test.delay()

    form = TestForm()
    return render(request, "django_celery/home.html",{"form" : form})

