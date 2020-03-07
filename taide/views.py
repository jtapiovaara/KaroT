from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from .models import TauluTaulu, KysyTaulusta

# Here are libraries for printing

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML


# Create your views here.
class TaideLista(generic.ListView):
    model = TauluTaulu


class MailiCreate(CreateView):
    model = KysyTaulusta
    fields = ['maili'
              ]


class Raportti(generic.ListView):
    model = KysyTaulusta


def html_to_pdf_view(request, *args):
    paragraphs = TauluTaulu.objects.filter(*args)
    html_string = render_to_string('taide/taide_lista_pdf.html', {'paragraphs': paragraphs})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/taide_lista.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('taide_lista.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="taide_lista.pdf"'
        return response

    return response


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







