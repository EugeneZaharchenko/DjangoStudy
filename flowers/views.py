from django.http import HttpResponse

from .models import Flower, Bouquet, Client
from uuid import uuid4
from decimal import Decimal

from django.contrib.auth.models import User

from django.core.files import File


def create_flower(request):
    rose = Flower()
    rose.description = "Троянда є представником сімейства різнокольорових," \
                       " роду Шипшина. Рослина в більшості випадків " \
                       "являє собою розгалужений чагарник, стебла" \
                       " якого вкриті шипами, троянда має зелене листя"
    rose.wiki_page = "посилання на вікі"
    rose.name = "Троянда червона"
    rose.save()
    return HttpResponse("Created!")


def create_client(request):
    client = Client.objects.create(**{
        'user': User.objects.get(pk=1),
        'second_email': 'admin@admin1.com',
        'name': 'MyName',
        'invoice': File(open('requirements.txt')),
        'user_uuid': uuid4(),
        'discount_size': Decimal("0.00052"),
        'client_ip': "192.0.2.1.",
    })
    return HttpResponse(client)


def get_flower(request):
    price = Bouquet.shop.get(id=1).price
    return HttpResponse(price)
