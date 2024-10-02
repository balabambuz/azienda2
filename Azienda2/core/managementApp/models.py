from django.db import models
from django.urls import reverse


class Sede1(models.Model):
    indirizzo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse('managementApp:dipendente_sede', args=[self.slug])

    def __str__(self):
        return self.indirizzo

class Azienda1(models.Model):
    nomeAzienda = models.CharField(max_length=200)
    immagine = models.ImageField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse('managementApp:dipendente_azienda', args=[self.slug])

    def __str__(self):
        return self.nomeAzienda

class Dipendente1(models.Model):
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    immagine = models.ImageField(blank=True)
    sede = models.ForeignKey(Sede1, on_delete=models.CASCADE)
    azienda = models.ForeignKey(Azienda1, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('managementApp:dipendente_detail', args=[self.nome])
    
    

    def __str__(self):
        return self.nome

class Ordine(models.Model):
    dipendente = models.ForeignKey(Dipendente1, on_delete=models.CASCADE)
    prezzo = models.IntegerField()









