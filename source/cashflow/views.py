from rest_framework import viewsets
from django.shortcuts import render
from .models import Cashflow, Status, Type, Category, Undercat, UndercatList
from .serializers import (
    StatusSerializer, TypeSerializer, CategorySerializer,
    UndercatSerializer, CashflowSerializer, UndercatListSerializer
)

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UndercatViewSet(viewsets.ModelViewSet):
    queryset = Undercat.objects.all()
    serializer_class = UndercatSerializer


class CashflowViewSet(viewsets.ModelViewSet):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer


class UndercatListViewSet(viewsets.ModelViewSet):
    queryset = UndercatList.objects.all()
    serializer_class = UndercatListSerializer