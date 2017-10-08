from django.db import models


class GlobalPermission(models.Model):
    class Meta:
        managed = False

        permissions = {
            ('app', 'Service desk right'),
        }
