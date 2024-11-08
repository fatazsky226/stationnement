from django.db import models

class Parking(models.Model):
    nom_parking = models.CharField(max_length=100)
    nombre_place = models.IntegerField()
    statut = models.CharField(max_length=10, choices=[('libre', 'Libre'), ('occupé', 'Occupé')])

    def __str__(self):
        return self.nom_parking



class Place(models.Model):
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, related_name="places")
    numero_place = models.IntegerField(unique=True) 
    taille = models.CharField(max_length=20)
    type_place = models.CharField(max_length=10, choices=[('mobylette', 'Mobylette'), ('voiture', 'Voiture'), ('camion', 'Camion')])

    def __str__(self):
        return f"Place {self.numero_place} - {self.type_place} - {self.taille}"
