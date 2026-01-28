from datetime import date
from django.db import models



# Create your models here.
class Todo(models.Model):
    tile= models.CharField(verbose_name="Titulo",max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de entrega",null=True, blank=True)
    finished_at = models.DateField(null=True, blank=True)

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()

    class Meta:
        ordering = ["deadline"]

