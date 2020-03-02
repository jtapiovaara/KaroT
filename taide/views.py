from django.views import generic
from django.shortcuts import render, redirect
from .models import TauluTaulu, KysyTaulusta
from .forms import Taulukysymys

# Here are libraries for printing

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML


# Create your views here.
class TaideLista(generic.ListView):
    model = TauluTaulu


# def maili(response):
#     if response.method == 'POST':
#         form = Taulukysymys(response.POST)
#         if form.is_valid():
#             n = form.cleaned_data['maili']
#             tunnus = n.partition("@")[0]
#             t = KysyTaulusta(maili=n)
#             t.save()
#             subject = 'Uusi seuraaja'
#             message = t.maili
#             tunnus = message.partition("@")[0]
#             eemaili = message
#             print(tunnus+' ja '+eemaili+' ovat uuden seuraajan tiedot')
#
#             return render(response, 'taide/index_mail.html', {'form': message})
#     else:
#         form = Taulukysymys()
#     return render(response, 'taide/osoite.html', {'form': form})


class Raportti(generic.ListView):
    model = KysyTaulusta


def html_to_pdf_one_view(request, pk):
    paragraphs = TauluTaulu.objects.filter(pk=pk)
    html_string = render_to_string('taide/pdf_template.html', {'paragraphs': paragraphs})
    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/taulusi.pdf')

    fs = FileSystemStorage('/tmp')

    with fs.open('taulusi.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="taulusi.pdf"'
        return response

    return response







