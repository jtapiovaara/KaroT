from django.urls import path
from . import views


app_name = 'taide'

urlpatterns = [
    path('', views.TaideLista.as_view(), name='home'),
    path('maili/<pk>', views.MailiCreate, name='maili'),
    # path('index_mail', views.MailiOk, name='mailiok'),
    path('printed/', views.html_to_pdf_view, name='printlist'),
    path('print/<int:pk>', views.html_to_pdf_one_view, name='printrequest'),
    path('raportti', views.Raportti.as_view(), name='raportti'),
    path('myydyt', views.sold, name='myydyt')
    ]
