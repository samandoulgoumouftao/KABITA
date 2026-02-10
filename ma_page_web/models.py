from django.db import models
from django.utils.text import slugify

class Profil(models.Model):
    nom = models.CharField(max_length=100)
    metier = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='profil/')
    email = models.EmailField()

    def __str__(self):
        return self.nom

class Article(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='articles/')
    resume = models.TextField(max_length=300)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre

class Produit(models.Model):
    CATEGORIES = [
        ('ORDINATEUR', 'Ordinateur'),
        ('TELEPHONE', 'Téléphone'),
    ]
    nom = models.CharField(max_length=200)
    categorie = models.CharField(max_length=20, choices=CATEGORIES)
    prix = models.DecimalField(max_digits=10, decimal_places=0) # FCFA
    description = models.TextField()
    image = models.ImageField(upload_to='produits/', blank=True, null=True)

    def get_image_url(self):
        if self.image:
            return self.image.url
        # Images par défaut dans ton dossier static/images/
        if self.categorie == 'ORDINATEUR':
            return '/static/images/tao_ordinateur.png'
        return '/static/images/tao_telephone.png'

    def __str__(self):
        return f"{self.nom} ({self.categorie})"
    from django.db import models

class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.nom} - {self.sujet}"