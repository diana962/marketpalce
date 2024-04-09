# Generated by Django 5.0.3 on 2024-04-09 09:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(blank=True, max_length=1500)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('preview', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('catalog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clothes', to='catalog.catalog')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Clothes',
                'verbose_name_plural': 'Clothes',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='ClothesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.clothes')),
            ],
        ),
    ]
