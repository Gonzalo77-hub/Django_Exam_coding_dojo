# Generated by Django 3.2.5 on 2021-09-07 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('role', models.CharField(choices=[('user', 'User'), ('admin', 'Admin')], max_length=255)),
                ('password', models.CharField(max_length=70)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('q_cont', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='app_examen.user')),
                ('like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='app_examen.user')),
            ],
        ),
    ]