from django.db import models

class ObjModel(models.Model):

    title = models.CharField(max_length=50)
    article=models.CharField(max_length=150)
    width=models.IntegerField()
    height=models.IntegerField()
    depth=models.IntegerField()
    modelFile = models.FileField(upload_to='models/')

    
    def __str__(self) -> str:
        return self.title