from django.db import models


class Cashflow(models.Model):
    creation_time = models.DateTimeField(auto_now=True)
    status_id = models.ForeignKey('Status', on_delete=models.CASCADE, null=False)
    type_id = models.ForeignKey('Type', on_delete=models.CASCADE, null=False)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, null=False)
    summ = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(null=True)


class Status(models.Model):
    name = models.CharField(max_length=128)


class Type(models.Model):
    name = models.CharField(max_length=128)


class Category(models.Model):
    name = models.CharField(max_length=128)


class Undercat(models.Model):
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, null=False, related_name='children')
    name = models.CharField(max_length=128)


class UndercatList(models.Model):
    cashflow_id = models.ForeignKey('Cashflow', on_delete=models.CASCADE, null=False)
    undercat_id = models.ForeignKey('Undercat', on_delete=models.CASCADE, null=False)
