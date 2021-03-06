# Generated by Django 3.1 on 2020-08-24 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.CharField(max_length=12)),
                ('descripcion', models.CharField(max_length=500)),
                ('numero_pedido', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('fecha_salida', models.DateField()),
                ('pendiente', models.BooleanField()),
                ('entregado', models.BooleanField()),
                ('fecha_entrega', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_cliente', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=12)),
                ('telefono', models.CharField(max_length=12)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Venta_Productos.productos')),
            ],
        ),
    ]
