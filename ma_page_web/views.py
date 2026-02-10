import resend
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .models import Profil, Article, MessageContact

# REMPLACE CECI PAR TA CLÉ COPIÉE (Garde les guillemets)
resend.api_key = "re_C8aasvre_3tfg5qNPAHhqJ4Q46wPj4MDF" 

def home(request):
    mon_profil = Profil.objects.first()
    mes_articles = Article.objects.all().order_by('-date_publication')[:2]
    
    if request.method == "POST":
        nom = request.POST.get('nom')
        email_client = request.POST.get('email')
        sujet_client = request.POST.get('sujet')
        message_client = request.POST.get('message')
        
        try:
            # 1. On enregistre en base de données (sécurité)
            MessageContact.objects.create(
                nom=nom, 
                email=email_client, 
                sujet=sujet_client, 
                message=message_client
            )
            
            # 2. On envoie l'email via Resend (vitesse)
            resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": "mouftaoa@gmail.com",
                "subject": f"KABITA (Accueil) : {sujet_client}",
                "html": f"<p><strong>Nom:</strong> {nom}</p><p><strong>Email:</strong> {email_client}</p><p><strong>Message:</strong> {message_client}</p>"
            })
            
            messages.success(request, "VOTRE MESSAGE A ÉTÉ REÇU ET ENVOYÉ AVEC SUCCÈS !")
        except Exception as e:
            print(f"Erreur: {e}")
            messages.error(request, "VOTRE MESSAGE A ÉTÉ ENREGISTRÉ MAIS L'ENVOI EMAIL A ÉCHOUÉ.")
            
        return redirect('home')

    return render(request, 'home.html', {'profil': mon_profil, 'articles': mes_articles})

def boutique(request):
    produits = [
        {'nom': 'Redmi 15C 256GB', 'cat': 'TELEPHONE', 'prix': '75 000', 'img': 'redmi_15c_256.jpg'},
        {'nom': 'Infinix Hot 60i 128GB', 'cat': 'TELEPHONE', 'prix': '80 000', 'img': 'infinix_hote_60i.jpg'},
        {'nom': 'Redmi 14C', 'cat': 'TELEPHONE', 'prix': '70 000', 'img': 'redmi_14c.jpg'},
        {'nom': 'HP Core i7', 'cat': 'ORDINATEUR', 'prix': '160 000', 'img': 'hp_corei3.jpg'},
        {'nom': 'Lenovo Core i3', 'cat': 'ORDINATEUR', 'prix': '100 000', 'img': 'lenovo_corei3.jpg'},
        {'nom': 'Dell Core i3', 'cat': 'ORDINATEUR', 'prix': '100 000', 'img': 'dell_corei3.jpg'},
        {'nom': 'Asus Core i5', 'cat': 'ORDINATEUR', 'prix': '190 000', 'img': 'asus_corei5.jpg'},
    ]
    return render(request, 'boutique.html', {'produits': produits})

def contact(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        email_client = request.POST.get('email')
        sujet_client = request.POST.get('sujet')
        message_client = request.POST.get('message')
         
        try:
            resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": "mouftaoa@gmail.com",
                "subject": f"SITE WEB KABITA (Contact) : {sujet_client}",
                "html": f"<h3>Nouveau message</h3><p><strong>De:</strong> {nom} ({email_client})</p><p><strong>Message:</strong> {message_client}</p>"
            })
            messages.success(request, "VOTRE MESSAGE A ÉTÉ ENVOYÉ AVEC SUCCÈS")
        except Exception as e:
            print(f"DEBUG RESEND ERROR: {e}")
            messages.error(request, "ERREUR LORS DE L'ENVOI")
        
        return redirect('contact')
        
    return render(request, 'contact.html')

def apropos(request):
    mon_profil = Profil.objects.first()
    return render(request, 'apropos.html', {'profil': mon_profil})