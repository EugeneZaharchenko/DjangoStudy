import os
from uuid import uuid4
from decimal import Decimal

from django.conf import settings
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.shortcuts import render

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files import File

from .models import Flower, Bouquet, Client
from .forms import MyForm, FormFromModel


def create_flower(request):
    rose = Flower()
    rose.count = 7
    # rose.count = 777777777777777777777777777777
    rose.description = "Троянда є представником сімейства різнокольорових," \
                       " роду Шипшина. Рослина в більшості випадків " \
                       "являє собою розгалужений чагарник, стебла" \
                       " якого вкриті шипами, троянда має зелене листя"
    rose.could_use_in_bouquet = True
    rose.wiki_page = "wiki"
    rose.name = "Троянда червона"
    rose.save()
    return HttpResponse("Created!")


# def create_client(request):
#     client = Client.objects.create(**{
#         # 'user': User.objects.get(pk=1),
#         'second_email': 'adminadmin1.com',
#         # 'second_email': 'admin@admin1.com',
#         'name': 'LongName' * 64,
#         'invoice': File(open('requirements.txt')),
#         'user_uuid': uuid4(),
#         'discount_size': Decimal("0.00052"),
#         # 'client_ip': "192.0.2.1.",
#         'client_ip': "192.0.2.1.wrong",
#     })
#     return HttpResponse(client)

def create_client(request):
    client = Client(**{
        'user': User.objects.get(pk=1),
        'second_email': 'admin@admin1.com',
        # 'second_email': 'adminadmin1.com',
        # 'name': 'LongName' * 64,
        'name': 'Name',
        'invoice': File(open('requirements.txt')),
        'user_uuid': uuid4(),
        'discount_size': Decimal("0.00052"),
        'client_ip': "192.0.2.1",
        # 'client_ip': "192.0.2.1.wrong",
    })
    try:
        client.full_clean()
    except ValidationError as e:
        return HttpResponse(e)
    else:
        client.save()
        return HttpResponse(client)


def get_flower(request):
    # price = Bouquet.shop.get(id=1).price
    usual_price = Bouquet.objects.get(id=1).price
    return HttpResponse(price)


# python3 manage.py shell
# from flowers.models import Client
# all_clients = Client.objects.all()
# list(all_clients)
# all_clients.delete()

def my_form(request):
    # return HttpResponse(MyForm().as_p())
    print(f'request.GET: {request.GET}')
    form = MyForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        print(form.cleaned_data)
        # file_path = os.path.join(settings.MEDIA_ROOT,
        #                          form.cleaned_data['profile_picture'].name)
        # with open(file_path, 'wb+') as local_file:
        #     for chunk in form.cleaned_data['profile_picture']:
        #         local_file.write(chunk)
    else:
        print(form.errors)

    return render(request, 'form_page.html', context={'form': form})


class MyFormView(FormView):
    form_class = MyForm
    template_name = "form_page.html"

    def get(self, request, *args, **kwargs):
        print(request.GET)
        return super().get(request, *args, **kwargs)


class ModelFormView(FormView):
    form_class = FormFromModel
    template_name = "model_from_page.html"
    success_url = reverse_lazy("modelform")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
