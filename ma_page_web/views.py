import resend
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .models import Profil, Article, MessageContact

# CLÉ API CONFIGURÉE
resend.api_key = "re_K3DBWneR_F2SnBtQfRrjgwzwmP4ttZetE" 

def home(request):
    # Gestion du formulaire (présent dans base.html ou home.html)
    if request.method == "POST":
        nom = request.POST.get('nom')
        email_client = request.POST.get('email')
        sujet_client = request.POST.get('sujet')
        message_client = request.POST.get('message')
        try:
            MessageContact.objects.create(nom=nom, email=email_client, sujet=sujet_client, message=message_client)
            resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": "mouftaoa@gmail.com",
                "subject": f"KABITA (Accueil) : {sujet_client}",
                "html": f"<p><strong>Nom:</strong> {nom}</p><p><strong>Message:</strong> {message_client}</p>"
            })
            messages.success(request, "MESSAGE ENVOYÉ AVEC SUCCÈS !")
        except Exception as e:
            messages.error(request, "ERREUR LORS DE L'ENVOI")
        return redirect('home')

    mon_profil = Profil.objects.first()
    mes_articles = Article.objects.all().order_by('-date_publication')[:2]
    return render(request, 'home.html', {'profil': mon_profil, 'articles': mes_articles})

def boutique(request):
    # Gestion du formulaire (si l'utilisateur clique sur envoyer depuis la boutique)
    if request.method == "POST":
        nom = request.POST.get('nom')
        email_client = request.POST.get('email')
        sujet_client = request.POST.get('sujet')
        message_client = request.POST.get('message')
        try:
            MessageContact.objects.create(nom=nom, email=email_client, sujet=sujet_client, message=message_client)
            resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": "mouftaoa@gmail.com",
                "subject": f"KABITA (Boutique) : {sujet_client}",
                "html": f"<p><strong>Nom:</strong> {nom}</p><p><strong>Message:</strong> {message_client}</p>"
            })
            messages.success(request, "MESSAGE ENVOYÉ DEPUIS LA BOUTIQUE !")
        except Exception as e:
            messages.error(request, "ERREUR LORS DE L'ENVOI")
        return redirect('boutique')

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
            MessageContact.objects.create(nom=nom, email=email_client, sujet=sujet_client, message=message_client)
            resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": "mouftaoa@gmail.com",
                "subject": f"KABITA (Contact) : {sujet_client}",
                "html": f"<h3>Message de {nom}</h3><p>{message_client}</p>"
            })
            messages.success(request, "VOTRE MESSAGE A ÉTÉ ENVOYÉ AVEC SUCCÈS")
        except Exception as e:
            messages.error(request, "ERREUR LORS DE L'ENVOI")
        return redirect('contact')
    return render(request, 'contact.html')

def apropos(request):
    # Gestion du formulaire (si l'utilisateur clique sur envoyer depuis la page À propos)
    if request.method == "POST":
        nom = request.POST.get('nom')
        email_client = request.POST.get('email')
        sujet_client = request.POST.get('sujet')
        message_client = request.POST.get('message')
        try:
            MessageContact.objects.create(nom=nom, email=email_client, sujet=sujet_client, message=message_client)
            resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": "mouftaoa@gmail.com",
                "subject": f"KABITA (A propos) : {sujet_client}",
                "html": f"<p><strong>Nom:</strong> {nom}</p><p><strong>Message:</strong> {message_client}</p>"
            })
            messages.success(request, "MESSAGE ENVOYÉ !")
        except Exception as e:
            messages.error(request, "ERREUR LORS DE L'ENVOI")
        return redirect('apropos')

    mon_profil = Profil.objects.first()
    return render(request, 'apropos.html', {'profil': mon_profil})