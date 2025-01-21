# Generated by Django 4.2.18 on 2025-01-21 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moto', models.CharField(max_length=100)),
                ('classroom', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Literature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('genre', models.CharField(max_length=50)),
                ('release_date', models.DateTimeField()),
                ('Author', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('surname', models.CharField(max_length=80)),
                ('student_id', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='student.group')),
            ],
        ),
        migrations.CreateModel(
            name='LiteratureRental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateTimeField(auto_now=True)),
                ('rent_giver', models.CharField(max_length=240)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='literature_rentals', to='student.literature')),
                ('rent_taker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='literature_rentals', to='student.access')),
            ],
        ),
        migrations.AddField(
            model_name='access',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='access', to='student.student'),
        ),
    ]
