from rest_framework import viewsets
from .models import Medication
from .serializers import MedicationSerializer

# MedicationViewSet crud
class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
