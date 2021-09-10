from django.contrib import messages
from django.db.models.aggregates import Count
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required,admin_requerido
from .models import *


@login_required
def index(request):

    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)

@admin_requerido
def administrador(request):

    context = {
        'saludo': 'ADMINISTRADOR'
    }
    return render(request, 'admin.html', context)
def page_edit(request, num):
    context = {"account": User.objects.get(id=num)
    
    }
    return render(request, 'profile.html', context)
    
def page_quote(request):
    context = {"quotes": Quote.objects.all(),
                "likes": Quote.objects.values_list('like', flat=True)
    }
    return render(request, 'quotes.html', context)

def add_quotes(request):

    errors = Quote.objects.quote_valid(request.POST)
    
    if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ("/quotes/")
    else:
        Quote.objects.create(autor= request.POST['autor'],
        q_cont= request.POST['quote_text'],
        creador= User.objects.get(id=request.session['usuario'] ['id']))
        return redirect('/quotes/')

def edit(request, id):

    errors = User.objects.validador_edit(request.POST)
    
    if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect (f"/edit_account/{id}/")
    else:
        ed_user = User.objects.get(id=id)
        ed_user.name = request.POST['edit_name']
        ed_user.last_name = request.POST['edit_last_name']
        ed_user.email = request.POST['edit_email']
        ed_user.save()
        return redirect("/quotes/")

def post_likes(request, num):
    quote = Quote.objects.get(id=num)
    user = User.objects.get(id= request.session['usuario'] ['id'])
    quote.like.add(user)

    return redirect("/quotes/")

def page_user(request, id):

    context = {'perfil': User.objects.get(id=id),
                'perfil_quotes': Quote.objects.filter(creador=id)
    
    }
    return render(request, 'user.html', context)