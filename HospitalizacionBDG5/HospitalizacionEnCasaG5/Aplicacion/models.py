from re import T
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
        username=username,
        password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Persona(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    identificacion = models.CharField('Identificacion', max_length=15, null=False, blank=False)
    nombre = models.CharField('Nombre', max_length=45, null=False, blank=False)
    apellido = models.CharField('Apellido', max_length=45, null=False, blank=False)
    telefono = models.FloatField('Telefono')
    email = models.EmailField('Email', max_length=45, null=False, blank=False)
    sexos = [('F','Femenino'), ('M', 'Masculino')]
    genero = models.CharField('Genero', max_length=1, choices=sexos, default='F')    
    roles = [('1', 'Paciente'), ('2', 'Médico'), ('3', 'Familiar'), ('4', 'Auxiliar'), ('5', 'Enfermera/o')]
    #Rol = models.CharField(max_length=45, null=False, blank=False)
    rol = models.CharField('Rol',max_length=1, choices=roles)
    username = models.CharField(max_length=45, null=False, blank=False, unique=True)
    password = models.CharField(max_length=256, null=False, blank=False) #La longitud es esa porque se almacena el Hash y no la contraseña del usuario

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
       
    objects = UserManager()
    USERNAME_FIELD = 'username'

    def nombrePersona(self):
        txt = "{0} {1}"
        return txt.format(self.nombre, self.apellido)

    def __str__(self):
        txt = "Nombre: {0} {1}"
        return txt.format(self.nombre, self.apellido)


class Familiar(models.Model):
    parentesco = models.CharField('Parentesco', max_length=45, null=False, blank=False)
    correo = models.CharField('Correo', max_length=45, null=False, blank=False)
    id = models.OneToOneField(Persona, null=False, blank=False, on_delete=models.CASCADE, primary_key= True)

    def parentescoFamiliar(self):
        txt = "Parentesco de familiar: {0}"
        return txt.format(self.parentesco)

    def __str__(self):
        txt = "{0} familiar con parentesco: {1}"
        return txt.format(Persona.nombrePersona(self.id) , self.parentesco)


class Medico(models.Model):
    especialidad = models.CharField('Especialidad', max_length=45, null=False, blank=False)
    id = models.OneToOneField(Persona, null=False, blank=False, on_delete=models.CASCADE, primary_key= True)
    registro = models.CharField('Registro', max_length=45, null=False, blank=False)

    def especialidadMedico(self):
        txt = "Especialidad de médico: {0}"
        return txt.format(self.especialidad)

    def __str__(self):
        txt = "{0} médico con especialidad: {1}"
        return txt.format(Persona.nombrePersona(self.id), self.especialidad)


class Paciente(models.Model):
    direccion = models.CharField('Direccion', max_length=45, null=False, blank=False)
    ciudad = models.CharField('Ciudad', max_length=45, null=False, blank=False)
    fecha_nacimiento = models.DateField()
    latitud = models.CharField('Latitud', max_length=45, null= True, blank= True)
    longitud = models.CharField('Longitud', max_length=45, null= True, blank= True)
    id = models.OneToOneField(Persona, null=False, blank=False, on_delete=models.CASCADE, primary_key= True)
    medicoId = models.OneToOneField(Medico, null=False, blank=False, on_delete=models.CASCADE)
    familiarId = models.OneToOneField(Familiar, null=False, blank=False, on_delete=models.CASCADE)

    def nombrePaciente(self):
        txt = "{0}"
        return txt.format(Persona.nombrePersona(self.id))

    def __str__(self):
        txt = "Paciente: {0} . {1}. {2}"
        return txt.format(Persona.nombrePersona(self.id), Medico.especialidadMedico(self.medicoId), Familiar.parentescoFamiliar(self.familiarId))


class Auxiliar(models.Model):
    id = models.OneToOneField(Persona, null=False, blank=False, on_delete=models.CASCADE, primary_key= True)
    codigo = models.CharField('Codigo',max_length=45, null=False, blank=False)

    def __str__(self):
        txt = "Auxiliar con código: {0}"
        return txt.format(self.codigo) 

class Enfermero(models.Model):
    id = models.OneToOneField(Persona, null=False, blank=False, on_delete=models.CASCADE, primary_key= True)
    codigo = models.CharField('Codigo', max_length=45, null=False, blank=False)

    def __str__(self):
        txt = "Enfermera/o con código: {0}"
        return txt.format(self.codigo) 

class SignosVitales(models.Model):
    registroId = models.AutoField(auto_created=True, primary_key= True)
    oximetria = models.FloatField('Oximetría', null=True, blank=True)
    frecuenciaRespiratoria = models.FloatField('Frecuencia respiratoria',null=True, blank=True)
    frecuenciaCardiaca = models.FloatField('Frecuencia cardiaca', null=True, blank=True)
    temperatura = models.FloatField('Temperatura', null=True, blank=True)
    presionArterial = models.FloatField('Presion arterial', null=True, blank=True)
    glicemia = models.FloatField('Glicemia', null=True, blank=True)
    fecha = models.DateField()
    pacienteId = models.ForeignKey(Paciente, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        txt = "Registro de signos vitales del paciente {0}"
        return txt.format(Paciente.nombrePaciente(self.pacienteId))


class Diagnostico(models.Model):
    diagnosticoId = models.AutoField(auto_created=True, primary_key= True)
    descripcion = models.CharField('Descripción', max_length=45, null=False, blank=False)
    sugerencia = models.CharField('Sugerencia', max_length=45, null=False, blank=False)
    Fecha = models.DateField()
    medico = models.ForeignKey(Medico, related_name='Medico',  null=False, blank=False, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, related_name='Paciente', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0}. Diagnóstico: {1}. Sugerencia: {2}."
        return txt.format(Paciente.nombrePaciente(self.paciente) ,self.descripcion, self.sugerencia)