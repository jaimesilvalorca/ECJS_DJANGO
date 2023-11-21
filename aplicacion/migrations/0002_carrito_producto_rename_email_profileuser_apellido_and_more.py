# Generated by Django 4.2.4 on 2023-11-20 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('imagen', models.TextField(blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='profileuser',
            old_name='email',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='profileuser',
            old_name='lastname',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='profileuser',
            old_name='name',
            new_name='nombre',
        ),
        migrations.CreateModel(
            name='ProfileAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('direccion_envio', models.TextField()),
                ('total', models.IntegerField()),
                ('carrito', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.carrito')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.producto')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(through='aplicacion.ItemCarrito', to='aplicacion.producto'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.profileuser'),
        ),
    ]
