from django.db import models

class ColaboradorModel(models.Model):
    nome = models.TextField(max_length=255)
    score = models.TextField(max_length=255)
    senha = models.TextField(max_length=255)
    id_chefe = models.IntegerField(null=True)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = "colaborador"
