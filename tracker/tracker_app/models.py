from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def _str_(self):
        return self.name

class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    note = models.TextField(blank=True, null=True)

    def _str_(self):
        return f"{self.title} - {self.amount}"