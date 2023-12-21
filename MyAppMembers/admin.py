from django.contrib import admin
from .models import Membros


class memb(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "data_entrada", "telefone")


# Register your models here.
admin.site.register(Membros, memb)
