from rest_framework.views import APIView
from rest_framework.response import Response
from records.models import Record
from django.db.models import Sum

class SummaryView(APIView):
    def get(self, request):
        income = Record.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        expense = Record.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

        net = income - expense

        categories = Record.objects.values('category').annotate(total=Sum('amount'))

        return Response({
            "total_income": income,
            "total_expense": expense,
            "net_balance": net,
            "category_totals": categories
        })