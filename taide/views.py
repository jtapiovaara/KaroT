from django.views import generic
from django.shortcuts import render
from .models import TauluTaulu, KysyTaulusta

# Here are libraries for printing

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from taide.forms import Tiedustelu

from weasyprint import HTML


# Create your views here.
class TaideLista(generic.ListView):
    model = TauluTaulu

    def onsale(self):
        return TauluTaulu.objects.filter(tila__exact='Vapaa')

    def onexhibit(self):
        return TauluTaulu.objects.filter(tila__exact='Näyttelyssä')


def sold(request):
    myynti = TauluTaulu.objects.filter(tila__exact='Myyty')
    context = {
        'myynti': myynti
    }
    return render(request, 'taide/myyntiraportti.html', context)


def MailiCreate(request, pk):

    err_msg = ''
    message = ''
    kysytty = TauluTaulu.objects.prefetch_related('kysytaulusta_set').get(id=pk)

    fields = [
        'tiedustelu',
        'maili'
    ]

    if request.method == 'POST':
        form = Tiedustelu(request.POST)
        if form.is_valid():
            form.save()
            message = 'Kiitos, sähköpostiisi toimitetaan lisää tietoja taulusta.'
            print(form)
        else:
            message = err_msg
    form = Tiedustelu()

    context = {
        'message': message,
        'form': form,
        'kysytty': kysytty
    }
    return render(request, 'taide/kysytaulusta_form.html', context)


class Raportti(generic.ListView):
    model = KysyTaulusta


def html_to_pdf_view(request, *args):
    paragraphs = TauluTaulu.objects.filter(*args)
    html_string = render_to_string('taide/taide_lista_pdf.html', {'paragraphs': paragraphs})

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
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
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/taulusi.pdf')

    fs = FileSystemStorage('/tmp')

    with fs.open('taulusi.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="taulusi.pdf"'
        return response

    return response







