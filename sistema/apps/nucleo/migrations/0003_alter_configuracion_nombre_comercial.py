from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nucleo", "0002_configuracion_permitir_pago_parcial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="configuracion",
            name="nombre_comercial",
            field=models.CharField(default="PIZZA BELL", max_length=120, verbose_name="Nombre comercial"),
        ),
    ]
