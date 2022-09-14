from django.contrib import admin
from Modulos.Hospital.models import *

# Register your models here.

admin.site.register(Persona)
admin.site.register(Paciente)
admin.site.register(Familiar)
admin.site.register(Medico)
admin.site.register(Auxiliar)
admin.site.register(SignosVitales)
admin.site.register(Diagnostico)
