from django.contrib import admin
from .models import Profil, Article
from .models import MessageContact

admin.site.register(Profil)
admin.site.register(Article)
@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoi') # Les colonnes que tu verras