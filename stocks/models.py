from django.db import models

class Stock(models.Model):
  name = models.CharField(max_length=10, null=True, blank=True)
  price = models.FloatField()
  moment = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.name)