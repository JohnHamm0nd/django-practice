# Generated by Django 3.0.3 on 2020-03-14 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VL', '0003_auto_20200314_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visuallocalization',
            name='pred_country',
            field=models.CharField(blank=True, default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visuallocalization',
            name='true_country',
            field=models.CharField(blank=True, choices=[('0', '호주'), ('1', '한국'), ('2', '프랑스'), ('3', '이탈리아'), ('4', '미국'), ('5', '나도 몰라')], max_length=20),
        ),
    ]
