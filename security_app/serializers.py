from rest_framework import serializers
from .models import Vulnerability

class VulnerabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerability
        fields = '__all__'  # Incluye todos los campos del modelo

class FixedVulnerabilitySerializer(serializers.Serializer):
    cve_ids = serializers.ListField(child=serializers.CharField())