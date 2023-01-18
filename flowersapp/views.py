from flowersapp.models import Consultation, Buyer

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')


def card(request):
    return render(request, 'card.html')


def catalog(request):
    return render(request, 'catalog.html')


@csrf_exempt
def consultation(request):
    full_name = request.POST.get("fname")
    phonenumber = request.POST.get("tel")

    consultation = Consultation.objects.create(
        full_name=full_name,
        phonenumber=phonenumber
    )

    Buyer.objects.get_or_create(
        full_name=full_name,
        phonenumber=phonenumber,
        сonsultation=consultation
    )

    return render(request, 'consultation.html')


def order(request):
    return render(request, 'order.html')


def order_step(request):
    return render(request, 'order-step.html')


def quiz(request):
    return render(request, 'quiz.html')


def quiz_step(request):
    return render(request, 'quiz-step.html')


def result(request):
    return render(request, 'result.html')
