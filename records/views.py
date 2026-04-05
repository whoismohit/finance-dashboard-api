from rest_framework import viewsets
from .models import Record
from .serializers import RecordSerializer
from .permissions import IsAdmin, IsAnalystOrAdmin
from rest_framework.permissions import IsAuthenticated

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Record.objects.all()

        type_param = self.request.query_params.get('type')
        category = self.request.query_params.get('category')
        date = self.request.query_params.get('date')

        if type_param:
            queryset = queryset.filter(type=type_param)
        if category:
            queryset = queryset.filter(category=category)
        if date:
            queryset = queryset.filter(date=date)

        return queryset

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        return [IsAnalystOrAdmin()]