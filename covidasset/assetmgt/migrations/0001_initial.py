# Generated by Django 3.0.5 on 2020-04-12 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('asset_id', models.IntegerField(primary_key=True, serialize=False)),
                ('asset_name', models.CharField(max_length=250, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('district_id', models.IntegerField(primary_key=True, serialize=False)),
                ('district_name', models.CharField(max_length=250, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.IntegerField(primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(max_length=250)),
                ('hospital_type', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('contact_number', models.CharField(max_length=250)),
                ('doctors', models.IntegerField()),
                ('healthworkers', models.IntegerField()),
                ('latitude', models.CharField(max_length=250)),
                ('longitude', models.CharField(max_length=250)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assetmgt.District')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.IntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=250, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assetmgt.Hospital')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assetmgt.State'),
        ),
        migrations.CreateModel(
            name='AssetMgt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_total', models.IntegerField()),
                ('asset_utilized', models.IntegerField(default=0, null=True)),
                ('asset_balance', models.IntegerField(default=0, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('asset_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assetmgt.Asset')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assetmgt.Hospital')),
            ],
        ),
    ]
