from urllib import request, response
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Aplicacion.serializers import *

from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from Aplicacion.models import *

# Create your views here.

class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all() #Acá se le dice al serialziador que coja todos los parámetros
    serializer_class = PersonaSerializer
    # permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        print("GET a todos los usuarios del sistema")
        queryset = self.get_queryset() #Acá se piden todos los objetos
        serializer = PersonaSerializer(queryset, many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data) #La respuesta es la data que trae e serializador
    
class PersonaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    lookup_field = 'id' #Campo con el que se realiza la busqueda de objetos
    lookup_url_kwarg = 'pk' #Nombre dado en la URL para el argumento
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        print("GET a usuario")

        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token,verify=False)

        # if valid_data['user_id'] != kwargs['pk']:
        #     stringResponse = {'detail':'Unauthorized Request'}
        #     return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
            
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a usuario")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print("PATCH a usuario")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print("DELETE a usuario")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().delete(request, *args, **kwargs)

class MedicoListCreate(generics.ListCreateAPIView):
    queryset = Medico.objects.all() 
    serializer_class = MedicoSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los médicos del sistema")
        queryset = self.get_queryset() #Acá se piden todos los objetos
        serializer = MedicoSerializer(queryset, many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data) #La respuesta es la data que trae e serializador


    def post(self, request, *args, **kwargs):
        print("POST a un médico")
        print(request.data)
        personaData = request.data.pop('Persona') #Pide los datos y extrae los datos de persona dejando como sobrante los datos de médico 
        serializerP  = PersonaSerializer(data=personaData) #Se añaden datos a serializador
        serializerP.is_valid(raise_exception=True) #Se verifica que los datos son válidos
        Persona = serializerP.save() #Si todo está válido se guarda
        medData = request.data #Acá se pide la data sobrante que corresponde a los campos de médico
        medData.update({"id":Persona.id}) #Se agrega la llave desde la tabla de persona para relacionar las tablas
        serializerMed = MedicoSerializer(data=medData) #Se añaden datos a serializador de médico
        serializerMed.is_valid(raise_exception=True) #El serializador verifica los datos de médico
        serializerMed.save() #Si todo esta correcto agrega los datos de médico a la base.
        return Response(status=status.HTTP_201_CREATED) #Da esta respuesta si se creó correctamente, para añadir otras respuestas se puede ver la documentación


        tokenData = {"username":request.data["username"],
                    "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData) #Genera un token asociado al username y el password en las tablas especiales que se generan en la migración
        tokenSerializer.is_valid(raise_exception=True) #Mira si es válido

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED) #Saca la respuesta con el token serilizer no con el serializer del rol

class MedicoRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a médico")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a xxxxxxx")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print("PUT a xxxxxxx")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().patch(request, *args, **kwargs)

class FamiliarListCreate(generics.ListCreateAPIView):
    queryset = Familiar.objects.all() 
    serializer_class = FamiliarSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los familiares del sistema")
        queryset = self.get_queryset() #Acá se piden todos los objetos
        serializer = FamiliarSerializer(queryset, many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data) #La respuesta es la data que trae e serializador


    def post(self, request, *args, **kwargs):
        print("POST a un familiar")
        print(request.data)
        personaData = request.data.pop('Persona') #Pide los datos y extrae los datos de persona dejando como sobrante los datos de médico 
        serializerP  = PersonaSerializer(data=personaData) #Se añaden datos a serializador
        serializerP.is_valid(raise_exception=True) #Se verifica que los datos son válidos
        Persona = serializerP.save() #Si todo está válido se guarda
        endData = request.data #Acá se pide la data sobrante que corresponde a los campos de médico
        endData.update({"id":Persona.id}) #Se agrega la llave desde la tabla de persona para relacionar las tablas
        serializerEnd = FamiliarSerializer(data=endData) #Se añaden datos a serializador de médico
        serializerEnd.is_valid(raise_exception=True) #El serializador verifica los datos de médico
        serializerEnd.save() #Si todo esta correcto agrega los datos de médico a la base.
        return Response(status=status.HTTP_201_CREATED) #Da esta respuesta si se creó correctamente, para añadir otras respuestas se puede ver la documentación


        tokenData = {"username":request.data["username"],
                    "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
    
class FamiliarRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Familiar.objects.all()
    serializer_class = FamiliarSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a médico")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a xxxxxxx")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print("PUT a xxxxxxx")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().patch(request, *args, **kwargs)

class AuxiliarListCreate(generics.ListCreateAPIView):
    queryset = Auxiliar.objects.all() 
    serializer_class = AuxiliarSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los familiares del sistema")
        queryset = self.get_queryset() #Acá se piden todos los objetos
        serializer = AuxiliarSerializer(queryset, many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data) #La respuesta es la data que trae e serializador


    def post(self, request, *args, **kwargs):
        print("POST a un familiar")
        print(request.data)
        personaData = request.data.pop('Persona') #Pide los datos y extrae los datos de persona dejando como sobrante los datos de médico 
        serializerP  = PersonaSerializer(data=personaData) #Se añaden datos a serializador
        serializerP.is_valid(raise_exception=True) #Se verifica que los datos son válidos
        Persona = serializerP.save() #Si todo está válido se guarda
        endData = request.data #Acá se pide la data sobrante que corresponde a los campos de médico
        endData.update({"id":Persona.id}) #Se agrega la llave desde la tabla de persona para relacionar las tablas
        serializerEnd = AuxiliarSerializer(data=endData) #Se añaden datos a serializador de médico
        serializerEnd.is_valid(raise_exception=True) #El serializador verifica los datos de médico
        serializerEnd.save() #Si todo esta correcto agrega los datos de médico a la base.
        return Response(status=status.HTTP_201_CREATED) #Da esta respuesta si se creó correctamente, para añadir otras respuestas se puede ver la documentación


        tokenData = {"username":request.data["username"],
                    "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
    
class AuxiliarRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Auxiliar.objects.all()
    serializer_class = AuxiliarSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a médico")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a xxxxxxx")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print("PUT a xxxxxxx")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().patch(request, *args, **kwargs)

class EnfermeroListCreate(generics.ListCreateAPIView):
    queryset = Enfermero.objects.all() 
    serializer_class = EnfermeroSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los familiares del sistema")
        queryset = self.get_queryset() #Acá se piden todos los objetos
        serializer = EnfermeroSerializer(queryset, many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data) #La respuesta es la data que trae e serializador


    def post(self, request, *args, **kwargs):
        print("POST a un familiar")
        print(request.data)
        personaData = request.data.pop('Persona') #Pide los datos y extrae los datos de persona dejando como sobrante los datos de médico 
        serializerP  = PersonaSerializer(data=personaData) #Se añaden datos a serializador
        serializerP.is_valid(raise_exception=True) #Se verifica que los datos son válidos
        Persona = serializerP.save() #Si todo está válido se guarda
        endData = request.data #Acá se pide la data sobrante que corresponde a los campos de médico
        endData.update({"id":Persona.id}) #Se agrega la llave desde la tabla de persona para relacionar las tablas
        serializerEnd = EnfermeroSerializer(data=endData) #Se añaden datos a serializador de médico
        serializerEnd.is_valid(raise_exception=True) #El serializador verifica los datos de médico
        serializerEnd.save() #Si todo esta correcto agrega los datos de médico a la base.
        return Response(status=status.HTTP_201_CREATED) #Da esta respuesta si se creó correctamente, para añadir otras respuestas se puede ver la documentación


        tokenData = {"username":request.data["username"],
                    "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

class EnfermeroRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Enfermero.objects.all()
    serializer_class = EnfermeroSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a médico")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a xxxxxxx")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print("PUT a xxxxxxx")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().patch(request, *args, **kwargs)

class PacienteListCreate(generics.ListCreateAPIView):
    queryset = Paciente.objects.all() 
    serializer_class = PacienteSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los familiares del sistema")
        queryset = self.get_queryset() #Acá se piden todos los objetos
        serializer = PacienteSerializer(queryset, many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data) #La respuesta es la data que trae e serializador


    def post(self, request, *args, **kwargs):
        print("POST a un paciente")
        print(request.data)
        personaData = request.data.pop('Persona') #Pide los datos y extrae los datos de persona dejando como sobrante los datos de médico 
        serializerP  = PersonaSerializer(data=personaData) #Se añaden datos a serializador
        serializerP.is_valid(raise_exception=True) #Se verifica que los datos son válidos
        Persona = serializerP.save() #Si todo está válido se guarda
        endData = request.data #Acá se pide la data sobrante que corresponde a los campos de paciente
        endData.update({"id":Persona.id}) #Se agrega la llave desde la tabla de persona para relacionar las tablas
        serializerEnd = PacienteSerializer(data=endData) #Se añaden datos a serializador de paciente
        serializerEnd.is_valid(raise_exception=True) #El serializador verifica los datos de paciente
        serializerEnd.save() #Si todo esta correcto agrega los datos de paciente a la base.
        return Response(status=status.HTTP_201_CREATED) #Da esta respuesta si se creó correctamente, para añadir otras respuestas se puede ver la documentación


        tokenData = {"username":request.data["username"],
                    "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

class PacienteRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a médico")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a xxxxxxx")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print("PUT a xxxxxxx")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().patch(request, *args, **kwargs)



























