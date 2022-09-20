from Aplicacion.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('persona', PersonaViewset)
router.register('familiar', FamiliarViewset)
router.register('medico', MedicoViewset)
router.register('paciente', PacienteViewset)
router.register('auxiliar', AuxiliarViewset)
router.register('enfermero', EnfermeroViewset)
router.register('signosvitales', SignosVitalesViewset)
router.register('diagnostico', DiagnosticoViewset)

