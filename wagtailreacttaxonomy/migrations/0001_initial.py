# Generated by Django 3.1.1 on 2020-09-25 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaxonomyTerms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxonomy_id', models.CharField(max_length=255, unique=True)),
                ('terms_json', models.TextField()),
            ],
        ),
    ]
