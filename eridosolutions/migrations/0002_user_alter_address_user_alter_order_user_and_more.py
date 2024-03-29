# Generated by Django 5.0.1 on 2024-01-27 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eridosolutions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('auth0_user_id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eridosolutions.user'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eridosolutions.user'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eridosolutions.user'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eridosolutions.user'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
