# Generated by Django 3.2.6 on 2021-12-11 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0005_alter_idea_bank_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea_bank',
            name='desc',
            field=models.TextField(),
        ),
    ]
