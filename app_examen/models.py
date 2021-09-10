from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['name']) < 2:
            errors['firstname_len'] = "nombre debe tener al menos 2 caracteres de largo";

        if len(postData['last_name']) < 2:
            errors['firstname_len'] = "nombre debe tener al menos 2 caracteres de largo";

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "correo invalido"

        if not SOLO_LETRAS.match(postData['name']):
            errors['solo_letras'] = "solo letras en nombreporfavor"

        if len(postData['password']) < 4:
            errors['password'] = "contraseña debe tener al menos 8 caracteres"

        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "contraseña y confirmar contraseña no son iguales. "

        
        return errors

    def validador_edit(self, postData):
        
        errors = {}
        if postData['edit_name'] =='' or postData['edit_last_name'] =='' or postData['edit_email'] =='':
            errors['edit_campos'] = " los campos no pueden estar vacios"
        
        if User.objects.filter(email= postData['edit_email']).exclude(email=postData['edit_email']).exists():
            errors['email_exist'] = " El email que ingresaste ya existe"
        
        return errors


class User(models.Model):
    CHOICES = (
        ("user", 'User'),
        ("admin", 'Admin')
    )
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=255, choices=CHOICES)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class QuoteManager(models.Manager):

    def quote_valid(self, postData):
        
        errors = {}

        if len(postData['autor']) < 3:
            errors['autor'] = "El campo autor debe ser mayor a 3 caracteres"
        
        if len(postData['quote_text']) < 10:
            errors['quote_text'] = "El campo quote debe ser mayor a 10 caracteres"
        
        return errors
class Quote(models.Model):
    autor = models.CharField(max_length=50)
    q_cont = models.TextField(max_length=300)
    creador = models.ForeignKey(User, related_name="quotes", on_delete= models.CASCADE)
    like = models.ManyToManyField(User, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()
    

