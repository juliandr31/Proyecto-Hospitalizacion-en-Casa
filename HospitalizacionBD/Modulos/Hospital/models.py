from django.db import models

# Create your models here.

class Persona(models.Model):
    Id = models.CharField(max_length=15, primary_key= True, null=False, blank=False)
    Nombre = models.CharField(max_length=45, null=False, blank=False)
    Apellido = models.CharField(max_length=45, null=False, blank=False)
    Telefono = models.FloatField
    sexos = [('F','Femenino'), ('M', 'Masculino')]
    Genero = models.CharField(max_length=1, choices=sexos, default='F')
    Clave = models.CharField(max_length=45, null=False, blank=False)
    roles = [('1', 'Paciente'), ('2', 'Médico'), ('3', 'Familiar'), ('4', 'Auxiliar')]
    #Rol = models.CharField(max_length=45, null=False, blank=False)
    Rol = models.CharField(max_length=1, choices=roles)

    def nombrePersona(self):
        txt = "{0} {1}"
        return txt.format(self.Nombre, self.Apellido)

    def __str__(self):
        txt = "Nombre: {0} {1}"
        return txt.format(self.Nombre, self.Apellido)


class Familiar(models.Model):
    Parentesco = models.CharField(max_length=45, null=False, blank=False)
    Correo = models.CharField(max_length=45, null=False, blank=False)
    Id = models.OneToOneField(Persona, null=False, blank=False, on_delete=models.CASCADE, primary_key= True)

    def parentescoFamiliar(self):
        txt = "Parentesco de familiar: {0}"
        return txt.format(self.Parentesco)

    def __str__(self):
        txt = "{0} familiar con parentesco: {1}"
        return txt.format(Persona.nombrePersona(self.Id) , self.Parentesco)


class Medico(models.Model):
    Especialidad = models.CharField(max_length=45, null=False, blank=False)
    Id = models.OneToOneField(Persona, null=False, blank=False, on_delete=models.CASCADE, primary_key= True)
    Registro = models.CharField(max_length=45, null=False, blank=False)

    def especialidadMedico(self):
        txt = "Especialidad de médico: {0}"
        return txt.format(self.Especialidad)

    def __str__(self):
        txt = "{0} médico con especialidad: {1}"
        return txt.format(Persona.nombrePersona(self.Id), self.Especialidad)


class Paciente(models.Model):
    Direccion = models.CharField(max_length=45, null=False, blank=False)
    Ciudad = models.CharField(max_length=45, null=False, blank=False)
    Fecha_nacimiento = models.DateField()
    Latitud = models.CharField(max_length=45, null= True, blank= True)
    Longitud = models.CharField(max_length=45, null= True, blank= True)
    Id = models.OneToOneField(Persona, null=False, blank=False, on_delete=models.CASCADE, primary_key= True)
    MedicoId = models.OneToOneField(Medico, null=False, blank=False, on_delete=models.CASCADE)
    FamiliarId = models.OneToOneField(Familiar, null=False, blank=False, on_delete=models.CASCADE)

    def nombrePaciente(self):
        txt = "{0}"
        return txt.format(Persona.nombrePersona(self.Id))

    def __str__(self):
        txt = "Paciente: {0} . {1}. {2}"
        return txt.format(Persona.nombrePersona(self.Id), Medico.especialidadMedico(self.MedicoId), Familiar.parentescoFamiliar(self.FamiliarId))


class Auxiliar(models.Model):
    Id = models.OneToOneField(Persona, null=False, blank=False, on_delete=models.CASCADE, primary_key= True)
    Codigo = models.CharField(max_length=45, null=False, blank=False)

    def __str__(self):
        txt = "Auxiliar con código: {0}"
        return txt.format(self.Codigo) 



class SignosVitales(models.Model):
    RegistroId = models.AutoField(auto_created=True, primary_key= True)
    Oximetria = models.FloatField(null=True, blank=True)
    FrecuenciaRespiratoria = models.FloatField(null=True, blank=True)
    FrecuenciaCardiaca = models.FloatField(null=True, blank=True)
    Temperatura = models.FloatField(null=True, blank=True)
    PresionArterial = models.FloatField(null=True, blank=True)
    Glicemia = models.FloatField(null=True, blank=True)
    Fecha = models.DateField()
    PacienteId = models.ForeignKey(Paciente, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        txt = "Registro de signos vitales del paciente {0}"
        return txt.format(Paciente.nombrePaciente(self.PacienteId))


class Diagnostico(models.Model):
    DiagnosticoId = models.AutoField(auto_created=True, primary_key= True)
    Descripcion = models.CharField(max_length=45, null=False, blank=False)
    Sugerencia = models.CharField(max_length=45, null=False, blank=False)
    Fecha = models.DateField()
    Medico = models.ForeignKey(Medico, null=False, blank=False, on_delete=models.CASCADE)
    Paciente = models.ForeignKey(Paciente, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0}. Diagnóstico: {1}. Sugerencia: {2}."
        return txt.format(Paciente.nombrePaciente(self.Paciente) ,self.Descripcion, self.Sugerencia)