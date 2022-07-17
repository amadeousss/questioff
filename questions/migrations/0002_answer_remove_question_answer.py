# Generated by Django 4.0.4 on 2022-05-27 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('content', models.CharField(max_length=250)),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='questions.question')),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
    ]
