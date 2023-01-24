import folium
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from flowersapp.bot import tg_send_message
from flowersapp.models import Bouquet, BouquetQuiz, Buyer, Shop
from flowersapp.models import Consultation, Order, Payment
from .forms import UserRegistrationForm


KRASNOYARSK_CENTER = [56.010569, 92.852572]
DEFAULT_IMAGE_URL = (
    'https://media.istockphoto.com/id/182838201/ru/%D1%84%D0%BE%D1%82%D0%BE/daisy-%'
    'D0%BD%D0%B0-%D0%B1%D0%B5%D0%BB%D0%BE%D0%BC-%D1%81-%D0%BE%D0%B1%D1'
    '%82%D1%80%D0%B0%D0%B2%D0%BA%D0%B0.jpg?s=612x612&w=0&k=20&c=R6tOX'
    'pmIYQ_LLw4H8cju_ObMFefEjJlB9p2XCPA0Z3k='
)

def add_shop_on_map(folium_map, lat, lng, adress, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(20, 20),
    )
    folium.Marker(
        [lng, lat],
        icon=icon,
        popup=adress,
    ).add_to(folium_map)    

@csrf_exempt
def index(request):

    folium_map = folium.Map(location=KRASNOYARSK_CENTER, zoom_start=11)

    recommended_bouquets = Bouquet.objects.filter(recommend=True)

    working_shops = Shop.objects.filter(is_working=True)

    for working_shop in working_shops:
        add_shop_on_map(
                folium_map, 
                working_shop.lat,
                working_shop.lng,
                working_shop.address,
            )    
    site_map =folium_map._repr_html_()
    site_map = site_map[:90] + '80.5' + site_map[92:]

    if request.method == 'POST':
        full_name = request.POST.get('fname')
        phonenumber = request.POST.get('tel')

        buyer, created = Buyer.objects.get_or_create(
            phonenumber=phonenumber,
            defaults={
                'full_name': full_name},
        )
        Consultation.objects.create(
            full_name=full_name,
            phonenumber=phonenumber,
        ).buyer.set([buyer])
        tg_send_message(full_name, phonenumber)

    return render(
        request, 'index.html', context={
            'map': site_map,
            'bouquets': recommended_bouquets,
            'shops': working_shops,
            },
    )


def card(request, bouquet_url):
    bouquet = get_object_or_404(Bouquet, slug=bouquet_url)
    return render(request, 'card.html', context={'bouquet': bouquet})


def catalog(request):
    bouquets = Bouquet.objects.all()
    return render(request, 'catalog.html', context={'bouquets': bouquets})


@csrf_exempt
def consultation(request):
    if request.method == 'POST':
        full_name = request.POST.get('fname')
        phonenumber = request.POST.get('tel')

        buyer, created = Buyer.objects.get_or_create(
            phonenumber=phonenumber,
            defaults={
                'full_name': full_name},
        )
        Consultation.objects.create(
            full_name=full_name,
            phonenumber=phonenumber,
        ).buyer.set([buyer])
        main(full_name, phonenumber)

    return render(request, 'consultation.html')


@csrf_exempt
def order(request, slug):
    if request.method == "POST":
        full_name = request.POST.get('fname')
        phonenumber = request.POST.get('tel')
        address = request.POST.get('adres')
        delivery_time = request.POST.get('orderTime')

        сard_number = request.POST.get('cardNum')
        month = request.POST.get('cardMm')
        year = request.POST.get('cardGg')
        owner_name = request.POST.get('cardFname')
        cvv = request.POST.get('cardCvc')
        email = request.POST.get('mail')

        payment, created = Payment.objects.get_or_create(
            сard_number=сard_number,
            defaults={
                'owner_name': owner_name,
                'month': month,
                'year': year,
                'cvv': cvv
            }
        )

        bouquet = Bouquet.objects.get(id=slug)
        buyer, created = Buyer.objects.get_or_create(
            phonenumber=phonenumber,
            defaults={
                'full_name': full_name,
                'email': email,
                'payment': payment
            },
        )

        Order.objects.create(
            buyer=buyer,
            delivery_time=delivery_time,
            bouquet=bouquet,
            price=bouquet.price,
            address=address,
            payment=payment
        )

    return render(request, 'order.html')


@csrf_exempt
def order_step(request):
    print(request)
    return render(request, 'order-step.html')


@csrf_exempt
def quiz(request):
    return render(request, 'quiz.html')


@csrf_exempt
def quiz_step(request):
    return render(request, 'quiz-step.html')


def get_quiz_results(request):
    if request.method == 'GET':
        price = request.GET.get('price')
        request_prev = request.META.get('HTTP_REFERER')
        _, event = request_prev.split('?')
        _, event_value = event.split('=')
        return {
            'event': event_value,
            'price': price
        }


@csrf_exempt
def result(request):
    result = get_quiz_results(request)
    bouquet_quiz = BouquetQuiz.objects.filter(
        answer_event=result['event'],
        answer_price=result['price'])

    if not bouquet_quiz:
        bouquet_quiz = BouquetQuiz.objects.all()

    return render(request, 'result.html', context={"bouquet": bouquet_quiz[0].bouquet})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})
