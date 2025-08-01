# Generated by Django 5.2 on 2025-04-22 01:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('articulo_id', models.UUIDField(primary_key=True, serialize=False)),
                ('codigo_articulo', models.CharField(max_length=25)),
                ('codigo_barras', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=150)),
                ('presentacion', models.CharField(max_length=100)),
                ('estado', models.IntegerField()),
                ('stock', models.DecimalField(decimal_places=2, max_digits=12)),
                ('imagen', models.CharField(max_length=255)),
                ('grupo', models.ForeignKey(db_column='grupo_id', on_delete=django.db.models.deletion.RESTRICT, to='core.grupoarticulo')),
                ('linea', models.ForeignKey(db_column='linea_id', on_delete=django.db.models.deletion.RESTRICT, to='core.lineaarticulo')),
            ],
            options={
                'db_table': 'articulos',
                'ordering': ['codigo_articulo'],
            },
        ),
        migrations.CreateModel(
            name='CanalCliente',
            fields=[
                ('canal_id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre_canal', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'canal_cliente',
                'ordering': ['nombre_canal'],
            },
        ),
        migrations.CreateModel(
            name='ListaPrecios',
            fields=[
                ('articulo', models.OneToOneField(db_column='articulo_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.articulo')),
                ('precio_1', models.DecimalField(decimal_places=2, max_digits=12)),
                ('precio_2', models.DecimalField(decimal_places=2, max_digits=12)),
                ('precio_3', models.DecimalField(decimal_places=2, max_digits=12)),
                ('precio_4', models.DecimalField(decimal_places=2, max_digits=12)),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=12)),
                ('precio_costo', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
            options={
                'db_table': 'lista_precios',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.UUIDField(primary_key=True, serialize=False)),
                ('tipo_identificacion', models.CharField(max_length=1)),
                ('nro_identificacion', models.CharField(max_length=11)),
                ('nombres', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('correo_electronico', models.CharField(max_length=255)),
                ('nro_movil', models.CharField(max_length=15)),
                ('estado', models.IntegerField()),
                ('canal', models.ForeignKey(db_column='canal_id', on_delete=django.db.models.deletion.RESTRICT, to='core.canalcliente')),
            ],
            options={
                'db_table': 'clientes',
                'ordering': ['nro_identificacion'],
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('pedido_id', models.UUIDField(primary_key=True, serialize=False)),
                ('nro_pedido', models.IntegerField()),
                ('fecha_pedido', models.DateTimeField()),
                ('importe', models.DecimalField(decimal_places=2, max_digits=12)),
                ('estado', models.IntegerField()),
                ('cliente', models.ForeignKey(db_column='cliente_id', on_delete=django.db.models.deletion.RESTRICT, to='core.cliente')),
            ],
            options={
                'db_table': 'pedidos',
                'ordering': ['nro_pedido'],
            },
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('item_id', models.UUIDField(primary_key=True, serialize=False)),
                ('nro_item', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=12)),
                ('total_item', models.DecimalField(decimal_places=2, max_digits=12)),
                ('estado', models.IntegerField()),
                ('articulo', models.ForeignKey(db_column='articulo_id', on_delete=django.db.models.deletion.RESTRICT, to='core.articulo')),
                ('pedido', models.ForeignKey(db_column='pedido_id', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.pedido')),
            ],
            options={
                'db_table': 'items_pedido',
                'ordering': ['nro_item'],
            },
        ),
    ]
