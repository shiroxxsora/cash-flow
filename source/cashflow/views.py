from rest_framework import generics
from django.shortcuts import render
from .models import Cashflow
from .serializers import CashflowSerializer


class CashflowAPIView(generics.ListAPIView):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer
