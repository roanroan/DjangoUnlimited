# Generated by Django 2.2.6 on 2020-03-06 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('employer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
