from django.urls import path
from . import views


app_name = 'taide'

urlpatterns = [
    path('', views.TaideLista.as_view(), name='home'),
    # path('maili/<pk>', views.maili),
    # path('maili/maili/<pk>', views.maili),
    path('maili/<pk>', views.MailiCreate.as_view(), name='maili'),
    # path('index_mail', views.MailiCreate.as_view(), name='maili'),
    path('printed/', views.html_to_pdf_view, name='printlist'),
    path('print/<int:pk>', views.html_to_pdf_one_view, name='printrequest'),
    path('raportti', views.Raportti.as_view(), name='raportti')
    ]
