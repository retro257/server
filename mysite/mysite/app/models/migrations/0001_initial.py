# Generated by Django 3.2.5 on 2021-07-06 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('tittle', models.CharField(max_length=255)),
                ('content_text', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('text', models.TextField(max_length=255)),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='models.question')),
            ],
        ),
    ]