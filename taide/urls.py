from django.urls import path
from . import views


app_name = 'taide'

urlpatterns = [
    path('', views.TaideLista.as_view(), name='home'),
    path('taulu/<pk>', views.TaideDetail.as_view(), name='taulu'),
    path('maili/<pk>', views.mailicreate, name='maili'),
    path('näyttely/', views.html_to_pdf_view, name='exhibition'),
    path('print/<int:pk>', views.html_to_pdf_one_view, name='printrequest'),
    path('raportti', views.Raportti.as_view(), name='raportti'),
    path('myydyt', views.sold, name='myydyt')
    ]
