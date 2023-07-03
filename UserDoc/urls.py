from django.urls import path
from . import views
from django.conf.urls.static import static
import SOLUTECH

urlpatterns = [

    path('', views.HomeView.as_view(), name='accueil'),
    path('listeSalarie', views.ListeSalarie.as_view(), name='listeSalarie'),
    path('creationSalarie', views.CreationSalarie.as_view(), name='creationSalarie'),
    path('salarieStatistique', views.SalarieStatistique.as_view(), name='salarieStatistique'),
    path('conge', views.Conge.as_view(), name='conge'),
    path('suiviTemps', views.SuiviTemp.as_view(), name='suiviTemps'),
    path('calendrier', views.Calendrier.as_view(), name='calendrier'),
    path('paie', views.Paie.as_view(), name='paie'),
    path('parametre', views.Parametre.as_view(), name='parametre'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('registration', views.Registration.as_view(), name='registration'),
    path('profil', views.Profil.as_view(), name='profil'),
    path('document', views.Document.as_view(), name='document'),

]+static(SOLUTECH.settings.MEDIA_URL, document_root=SOLUTECH.settings.MEDIA_ROOT)
