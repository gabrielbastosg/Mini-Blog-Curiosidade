from django.contrib import admin
from .models import Curiosidade
# Register your models here.
@admin.register(Curiosidade)
class CuriosidadeAdmin(admin.ModelAdmin):
    list_display = ('titulo','categoria','data_criacao')
    search_fields = ('titulo','categoria')