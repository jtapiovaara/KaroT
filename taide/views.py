from django.views import generic
from django.shortcuts import render
from .models import TauluTaulu, KysyTaulusta
from django.db.models import Sum

# Here are libraries for printing

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from taide.forms import Tiedustelu

from weasyprint import HTML


# Create your views here.


class TaideLista(generic.ListView):
    """Taideteoksilla on neljä tilaa,(Myyty, Myytävänä, Näyttelyssä, Varastossa) kts DjangoAdmin ja Models"""
    model = TauluTaulu

    def onsale(self):
        return TauluTaulu.objects.filter(tila__exact='Myytävänä')

    def onexhibit(self):
        return TauluTaulu.objects.filter(tila__exact='Näyttelyssä')


class TaideDetail(generic.DetailView):
    model = TauluTaulu


def sold(request):
    myynti = TauluTaulu.objects.filter(tila__exact='Myyty')
    myyntitotal = TauluTaulu.objects.filter(tila__exact='Myyty').aggregate(Sum('hinta'))
    context = {
        'myynti': myynti,
        'myyntitotal': myyntitotal
    }
    return render(request, 'taide/myyntiraportti.html', context)


def mailicreate(request, pk):

    err_msg = 'Jokin meni pieleen, koitappa hetken päästä uudelleen.'
    message = ''
    kysytty = TauluTaulu.objects.prefetch_related('kysytaulusta_set').get(id=pk)

    # fields = [
    #     'tiedustelu',
    #     'maili'
    # ]

    if request.method == 'POST':
        print(kysytty.pk)
        form = Tiedustelu(request.POST)
        if form.is_valid():
            form.save()
            message = 'Kiitos, sähköpostiisi toimitetaan pian lisää tietoja taulusta.'
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
    """Näyttelylistan tulostaminen"""
    paragraphs = TauluTaulu.objects.filter(tila__exact='Näyttelyssä')
    html_string = render_to_string('taide/taide_lista_pdf.html', {'paragraphs': paragraphs})

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/taide_lista.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('taide_lista.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="taide_lista.pdf"'
        return response

    # return response


def html_to_pdf_one_view(request, pk):
    """Yksittäisen yhteydenoton jälkeinen tarjouskirje"""
    paragraphs = TauluTaulu.objects.filter(pk=pk)
    html_string = render_to_string('taide/pdf_template.html', {'paragraphs': paragraphs})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/taulusi.pdf')

    fs = FileSystemStorage('/tmp')

    with fs.open('taulusi.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="taulusi.pdf"'
        return response

    # return response







