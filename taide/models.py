from django.db import models


class TauluTaulu(models.Model):
    nimi = models.CharField(max_length=32)
    tarina = models.TextField(blank=True)
    materiaali = models.CharField(max_length=24, blank=True)
    koko = models.CharField(max_length=32, blank=True)
    vuosi = models.CharField(max_length=4, blank=True)
    hinta = models.IntegerField(null=True, blank=True)
    kuva = models.ImageField(blank=True)

    def __str__(self):
        return self.nimi

    class Meta:
        ordering = ('nimi',)


class KysyTaulusta(models.Model):
    maili = models.EmailField()
    taulu = models.CharField(max_length=64, blank=True)
    aika = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.maili


class TaiteilijaTaulu(models.Model):
    nimi = models.CharField(max_length=32)
    tilinro = models.CharField(max_length=64)
    viite = models.CharField(max_length=32)
    saajannimi = models.CharField(max_length=32)
    katuosoite = models.CharField(max_length=32)
    postinro = models.CharField(max_length=5)
    kunta = models.CharField(max_length=32)

    def __str__(self):
        return self.nimi
