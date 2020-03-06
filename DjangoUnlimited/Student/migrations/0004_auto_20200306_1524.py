# Generated by Django 2.2.6 on 2020-03-06 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_studentskill'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='personal_email',
            field=models.CharField(default='test@email.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='DOB',
            field=models.DateField(),
        ),
    ]
