from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from flowersapp.models import Bouquet, Buyer, Consultation


def index(request):
    recommended_bouquets = Bouquet.objects.filter(recommend=True)
    return render(request, 'index.html', context={"bouquets": recommended_bouquets})


def card(request, bouquet_url):
    bouquet = get_object_or_404(Bouquet, slug=bouquet_url)
    return render(request, 'card.html', context={"bouquet": bouquet})


def catalog(request):
    bouquets = Bouquet.objects.all()
    return render(request, 'catalog.html', context={"bouquets": bouquets})


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
