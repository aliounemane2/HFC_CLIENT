from django.shortcuts import render
from client.models import *

# Create your views here


def index(request):
    return render(request, 'index.html', {})

def saveinfo(request):
    user = User()

    user.civilite=request.POST["civilite"]
    user.prenom=request.POST["prenom"]
    user.nom=request.POST["nom"]
    user.dateNaiss=request.POST["dateNaiss"]
    user.lieuNaiss=request.POST["lieuNaiss"]
    user.telephone=request.POST["telephone"]
    user.adresse=request.POST["adresse"]
    user.situation_matrimoniale=request.POST["situation_matrimoniale"]
    user.ville=request.POST["ville"]
    user.email=request.POST["email"]
    user.profession=request.POST["profession"]
    user.medecin_traitant=request.POST["medecin_traitant"]
    user.victime_grave_accident=request.POST["victime_grave_accident"]
    user.autorisation_medicale_pour_programme_de_fitness_et_muscula=request.POST["autorisation_medicale_pour_programme_de_fitness_et_muscula"]
    user.autorisation_medicale_pour_programme_de_detente_de_hfc=request.POST["autorisation_medicale_pour_programme_de_detente_de_hfc"]
    user.sport_pratique_dans_le_passe=request.POST["sport_pratique_dans_le_passe"]
    user.sport_pratique_actuellement=request.POST["sport_pratique_actuellement"]
    user.etat_de_sante=request.POST["etat_de_sante"]
    user.problemes_majeurs_a_signaler_imperativement=request.POST["problemes_majeurs_a_signaler_imperativement"]
    user.maladies_graves_a_signaler=request.POST["maladies_graves_a_signaler"]
    user.problemes_de_poids=request.POST["problemes_de_poids"]
    user.coordonnees_completes_de_votre_medecin=request.POST["coordonnees_completes_de_votre_medecin"]
    user.poids=request.POST["poids"]
    user.taille=request.POST["taille"]
    user.rythme_cardiaque=request.POST["rythme_cardiaque"]
    user.tension=request.POST["tension"]
    user.besoin_specifique_et_attente_chez_hfc=request.POST["besoin_specifique_et_attente_chez_hfc"]
    user.souhaitez_vous_un_conseil_et_suivi_pers=request.POST["souhaitez_vous_un_conseil_et_suivi_pers"]
    user.souhaitez_vous_etre_suivi_par_un_professeur=request.POST["souhaitez_vous_etre_suivi_par_un_professeur"]
    user.souhaitez_vous_etre_suivi_par_un_professeur=request.POST["souhaitez_vous_etre_suivi_par_un_professeur"]
    user.comment_avez_vous_connu_hfc=request.POST["comment_avez_vous_connu_hfc"]
    user.save()

    return render(request, 'sucess.html', {})

