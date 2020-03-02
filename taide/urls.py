from django.urls import path
from . import views


app_name = 'taide'

urlpatterns = [
    path('', views.TaideLista.as_view(), name='home'),
    # path('maili/<pk>', views.maili),
    # path('maili/maili/<pk>', views.maili),
    # path('maili/', views.maili, name='maili'),
    # path('index_mail', views.maili, name='maili'),
    path('print/<int:pk>', views.html_to_pdf_one_view, name='printrequest'),
    path('raportti', views.Raportti.as_view(), name='raportti')
    ]
