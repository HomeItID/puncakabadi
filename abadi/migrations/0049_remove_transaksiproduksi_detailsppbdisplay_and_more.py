# Generated by Django 4.1.4 on 2024-06-24 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abadi', '0048_alter_pemusnahanbahanbaku_jumlah'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaksiproduksi',
            name='DetailSPPBDisplay',
        ),
        migrations.AddField(
            model_name='pemusnahanartikel',
            name='Keterangan',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pemusnahanbahanbaku',
            name='Keterangan',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transaksiproduksi',
            name='DetailSPKDisplay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='abadi.detailspkdisplay'),
        ),
        migrations.AddField(
            model_name='transaksiproduksi',
            name='KodeDisplay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='abadi.display'),
        ),
    ]
