# Generated by Django 3.0.6 on 2020-06-01 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0002_allow_null_foreignkeys'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendationSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.URLField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recommender.RecommendationSource'),
        ),
    ]
