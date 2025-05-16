from django.db import models

class User(models.Model):

    user_nome = models.CharField( max_length=100, default='')
    user_email = models.CharField(primary_key=True , default='')
    user_idade = models.CharField( default=0)


    def __str__(self):
        return f'Nome {self.user_nome} | E-mail: {self.user_email}'