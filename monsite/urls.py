from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ma_page_web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('boutique/', views.boutique, name='boutique'),
    path('a-propos/', views.apropos, name='apropos'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)