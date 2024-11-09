from django.contrib import admin

from app.models import Emprestimo, Equipamento, Usuario

admin.site.register(Usuario)
admin.site.register(Equipamento)
admin.site.register(Emprestimo)
