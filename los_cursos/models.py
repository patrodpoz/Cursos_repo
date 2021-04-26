from __future__ import unicode_literals
from django.db import models


class CursoManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData["name"]) < 5:
            errors['name'] = "Course name should have at least 5 characters"

        if len(postData["description"]) < 15:
            errors['description'] = "Description  should have at least 15 characters"

            
        return errors



class Descripcion(models.Model):
 
    description = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Curso(models.Model):
    name = models.CharField( max_length=50)
    description = models.OneToOneField(Descripcion, related_name="curso", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CursoManager()



