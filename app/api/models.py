from django.db import models


class CveModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=40000, null=True, blank=True)
    status = models.CharField(max_length=40000, null=True, blank=True)
    description = models.TextField(max_length=40000, null=True, blank=True)
    references = models.CharField(max_length=40000, null=True, blank=True)
    phase = models.CharField(max_length=40000, null=True, blank=True)
    votes = models.CharField(max_length=40000, null=True, blank=True)
    comments = models.CharField(max_length=40000, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Cve'
        ordering = ['id']
        db_table = 'api_cve'

    def __str__(self):
        return f'ID: {self.id}, \
         NAME: {self.name},\
         DESCRIPTION: {self.description[:10]}'
