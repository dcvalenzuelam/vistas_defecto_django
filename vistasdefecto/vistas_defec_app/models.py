from django.db import models

# Create your models here.
from django.db import models

class libros (models.Model):
    titulo = models.CharField(max_length=200)  
    autor = models.CharField(max_length=100) 
    fecha_publicacion = models.DateField()    

    def __str__(self):
        return self.title 