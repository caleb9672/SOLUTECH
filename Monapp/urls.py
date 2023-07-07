from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', views.HomeView.as_view(), name='accueil'),
    path('listeSalarie', views.ListeSalarie.as_view(), name='listeSalarie'),
    path('creationSalarie/<int:id>', views.CreationSalarie.as_view(), name='creationSalarie'),
    path("creationSalarie", views.CreationSalarie.as_view(), name='creationSalarie'),
    path('modificationSalarie', views.ModificationSalarie.as_view(), name='modificationSalarie'),
    path('salarieStatistique', views.SalarieStatistique.as_view(), name='salarieStatistique'),
    path('conge', views.Conge.as_view(), name='conge'),
    path('conge/<int:id>', views.Conge.as_view(), name='conge'),
    path('evaluationConge', views.EvaluationConge.as_view(), name='evaluationConge'),
    path('evaluationConge/<slug:valeur>', views.EvaluationConge.as_view(), name='evaluationConge'),
    path('congenotation/<int:id>', views.CongeNotation.as_view(), name='congenotation'),
    #path('demandeConge', views.DemandeConge.as_view(), name='demandeConge'),
    path('suiviTemps', views.SuiviTemp.as_view(), name='suiviTemps'),
    path('calendrier', views.Calendrier.as_view(), name='calendrier'),
    path('paie', views.Paie.as_view(), name='paie'),
    path('parametre', views.Parametre.as_view(), name='parametre'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout, name='logout'),
    path('registration', views.Registration.as_view(), name='registration'),
    path('profil', views.Profil.as_view(), name='profil'),
    path('document', views.Document.as_view(), name='document'),
    path('mesdocuments', views.Mesdocuments.as_view(), name='mesdocuments'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
