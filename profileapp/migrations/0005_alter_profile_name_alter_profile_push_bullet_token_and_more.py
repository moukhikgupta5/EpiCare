# Generated by Django 5.0 on 2023-12-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0004_seizures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='User', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='push_bullet_token',
            field=models.CharField(default='o.T5jj6vMn2KytwTfbVtmn8o8AzYiHpzfL', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(default='Epilypsey Patient', max_length=200, null=True),
        ),
    ]
