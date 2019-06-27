from myapp.models import MyModel
from myproject.celery import app


@app.task
def counter():
    instance, created = MyModel.objects.get_or_create(id=1)
    instance.counter += 1
    instance.save()
