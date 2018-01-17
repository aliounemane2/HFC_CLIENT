from django.db import models

# Create your models here.

class User(models.Model):

    civilite = models.CharField(max_length=255, blank=True, null=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    prenom = models.CharField(max_length=255, null=True, blank=True)
    dateNaiss = models.CharField(max_length=255, blank=True, null=True)
    lieuNaiss = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    situation_matrimoniale = models.CharField(max_length=255, blank=True, null=True)
    ville = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    medecin_traitant = models.CharField(max_length=255, blank=True, null=True)
    victime_grave_accident = models.CharField(max_length=255, blank=True, null=True)
    autorisation_medicale_pour_programme_de_fitness_et_muscula = models.CharField(max_length=255, blank=True, null=True)
    autorisation_medicale_pour_programme_de_detente_de_hfc = models.CharField(max_length=255, blank=True, null=True)
    sport_pratique_dans_le_passe = models.CharField(max_length=255, blank=True, null=True)
    sport_pratique_actuellement = models.CharField(max_length=255, blank=True, null=True)
    etat_de_sante = models.CharField(max_length=255, blank=True, null=True)
    problemes_majeurs_a_signaler_imperativement = models.CharField(max_length=255, blank=True, null=True)
    maladies_graves_a_signaler = models.CharField(max_length=255, blank=True, null=True)
    problemes_de_poids = models.CharField(max_length=255, blank=True, null=True)
    coordonnees_completes_de_votre_medecin = models.CharField(max_length=255, blank=True, null=True)
    poids = models.CharField(max_length=255, blank=True, null=True)
    taille = models.CharField(max_length=255, blank=True, null=True)
    rythme_cardiaque = models.CharField(max_length=255, blank=True, null=True)
    tension = models.CharField(max_length=255, blank=True, null=True)
    besoin_specifique_et_attente_chez_hfc = models.CharField(max_length=255, blank=True, null=True)
    souhaitez_vous_un_conseil_et_suivi_pers = models.CharField(max_length=255, blank=True, null=True)
    souhaitez_vous_etre_suivi_par_un_professeur = models.CharField(max_length=255, blank=True, null=True)
    comment_avez_vous_connu_hfc = models.CharField(max_length=255, blank=True, null=True)



    #favoriteContact = models.ForeignKey(FavouriteContact, null=True, blank=True)

    def __str__(self):
        return str(self.telephone)

