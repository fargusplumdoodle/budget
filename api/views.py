from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
import json


from .serializers import CategorySerializer, TransactionSerializer
from .models import Budget, Transaction
from .helper import budgets_sum_to_one

def dashboard(request):
    context = {}

    context['budgets'] = Budget.objects.all()
    context['budget_balanced'] = budgets_sum_to_one()

    return render(request, 'api/index.html', context=context)
