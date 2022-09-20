from rest_framework import viewsets
from Aplicacion import models
from Aplicacion import serializers

class PersonaViewset(viewsets.ModelViewSet):
    queryset = models.Persona.objects.all()
    serializer_class = serializers.PersonaSerializer

class FamiliarViewset(viewsets.ModelViewSet):
    queryset = models.Familiar.objects.all()
    serializer_class = serializers.FamiliarSerializer

class MedicoViewset(viewsets.ModelViewSet):
    queryset = models.Medico.objects.all()
    serializer_class = serializers.MedicoSerializer

class PacienteViewset(viewsets.ModelViewSet):
    queryset = models.Paciente.objects.all()
    serializer_class = serializers.PacienteSerializer

class AuxiliarViewset(viewsets.ModelViewSet):
    queryset = models.Auxiliar.objects.all()
    serializer_class = serializers.AuxiliarSerializer

class EnfermeroViewset(viewsets.ModelViewSet):
    queryset = models.Enfermero.objects.all()
    serializer_class = serializers.EnfermeroSerializer

class SignosVitalesViewset(viewsets.ModelViewSet):
    queryset = models.SignosVitales.objects.all()
    serializer_class = serializers.SignosVitalesSerializer

class DiagnosticoViewset(viewsets.ModelViewSet):
    queryset = models.Diagnostico.objects.all()
    serializer_class = serializers.DiagnosticoSerializer