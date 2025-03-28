from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import models
from .models import Vulnerability
from .serializers import VulnerabilitySerializer

class VulnerabilityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para visualizar y listar vulnerabilidades.
    Solo permite operaciones de lectura.
    """
    queryset = Vulnerability.objects.all()
    serializer_class = VulnerabilitySerializer

    @action(detail=False, methods=['post'])
    def mark_as_fixed(self, request):
        """
        Endpoint para marcar una o varias vulnerabilidades como fixeadas.
        Recibe una lista de CVE IDs en el cuerpo de la petición.
        """
        cve_ids_to_fix = request.data.get('cve_ids', [])
        updated_count = Vulnerability.objects.filter(cve_id__in=cve_ids_to_fix).update(fixed=True)
        return Response({'message': f'{updated_count} vulnerabilidades marcadas como fixeadas.'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def fixed_excluded(self, request):
        """
        Endpoint para listar vulnerabilidades que no han sido marcadas como fixeadas.
        """
        queryset = Vulnerability.objects.filter(fixed=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def summary_by_severity(self, request):
        """
        Endpoint para obtener información sumarizada de vulnerabilidades por severidad.
        """
        summary = Vulnerability.objects.values('severity').annotate(count=models.Count('severity'))
        return Response(summary)