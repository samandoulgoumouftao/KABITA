from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Profil, Article

def home(request):
    mon_profil = Profil.objects.first()
    # On affiche seulement les 2 derniers articles sur l'accueil
    mes_articles = Article.objects.all().order_by('-date_publication')[:2]
    
    if request.method == "POST":
        nom = request.POST.get('nom')
        email_client = request.POST.get('email')
        sujet_client = request.POST.get('sujet')
        message_client = request.POST.get('message')
        
        sujet_final = f"SITE WEB KABITA : {sujet_client}" 
        corps_final = f"De: {nom} ({email_client})\n\nMessage:\n{message_client}"
        
        try:
            send_mail(sujet_final, corps_final, settings.EMAIL_HOST_USER, ['mouftaoa@gmail.com'])
            messages.success(request, "VOTRE MESSAGE A ÉTÉ ENVOYÉ AVEC SUCCÈS")
        except:
            messages.error(request, "ERREUR LORS DE L'ENVOI")
        return redirect('home')

    return render(request, 'home.html', {
        'profil': mon_profil, 
        'articles': mes_articles
    })

def boutique(request):
    # TA LISTE DE PRODUITS (Tu peux changer les noms, prix et images ici directement)
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
        
        sujet_final = f"SITE WEB KABITA : {sujet_client}" 
        corps_final = f"De: {nom} ({email_client})\n\nMessage:\n{message_client}"
         
        try:
            send_mail(sujet_final, corps_final, settings.EMAIL_HOST_USER, ['mouftaoa@gmail.com'])
            messages.success(request, "VOTRE MESSAGE A ÉTÉ ENVOYÉ AVEC SUCCÈS")
        except:
            messages.error(request, "ERREUR LORS DE L'ENVOI")
        return redirect('contact')
        
    return render(request, 'contact.html')
def apropos(request):
    # On peut aussi passer le profil ici si tu veux utiliser {{ profil.nom }}
    from .models import Profil
    mon_profil = Profil.objects.first()
    return render(request, 'apropos.html', {'profil': mon_profil})