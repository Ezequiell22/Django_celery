from celery import shared_task
from stocks.models import Stock

@shared_task
def task_x(param1):
  Stock.objects.create(
    name=param1,
    price=float(10)
  )
  return param1