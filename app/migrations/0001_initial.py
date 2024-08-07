# Generated by Django 5.0.6 on 2024-07-06 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comport_settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_port', models.CharField(max_length=50)),
                ('baud_rate', models.IntegerField()),
                ('bytesize', models.IntegerField()),
                ('stopbits', models.IntegerField()),
                ('parity', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='consolidate_with_srno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_model', models.CharField(max_length=100)),
                ('parameter_name', models.CharField(max_length=100)),
                ('operator', models.CharField(max_length=100)),
                ('formatted_from_date', models.CharField(max_length=100)),
                ('formatted_to_date', models.CharField(max_length=100)),
                ('machine', models.CharField(max_length=100)),
                ('vendor_code', models.CharField(max_length=100)),
                ('job_no', models.CharField(max_length=100)),
                ('shift', models.CharField(max_length=100)),
                ('current_date_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='consolidate_without_srno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_model', models.CharField(max_length=100)),
                ('parameter_name', models.CharField(max_length=100)),
                ('operator', models.CharField(max_length=100)),
                ('formatted_from_date', models.CharField(max_length=100)),
                ('formatted_to_date', models.CharField(max_length=100)),
                ('machine', models.CharField(max_length=100)),
                ('vendor_code', models.CharField(max_length=100)),
                ('shift', models.CharField(max_length=100)),
                ('current_date_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='find',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probe_id', models.CharField(max_length=50, unique=True)),
                ('low_ref', models.JSONField(default=list)),
                ('low_count', models.JSONField(default=list)),
                ('high_ref', models.JSONField(default=list)),
                ('high_count', models.JSONField(default=list)),
                ('coefficent', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='jobwise_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_model', models.CharField(max_length=100)),
                ('job_no', models.CharField(max_length=100)),
                ('current_date_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='mastering_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probe_no', models.CharField(max_length=100)),
                ('a', models.FloatField()),
                ('b', models.FloatField()),
                ('e', models.FloatField()),
                ('d', models.FloatField()),
                ('o1', models.FloatField()),
                ('parameter_name', models.CharField(max_length=100)),
                ('selected_value', models.CharField(max_length=100)),
                ('selected_mastering', models.CharField(max_length=100)),
                ('date_time', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MasterIntervalSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timewise', models.BooleanField(default=False)),
                ('componentwise', models.BooleanField(default=False)),
                ('hour', models.IntegerField(blank=True, null=True)),
                ('minute', models.IntegerField(blank=True, null=True)),
                ('component_no', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='measure_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_model', models.CharField(max_length=100)),
                ('operator', models.CharField(max_length=100)),
                ('machine', models.CharField(max_length=100)),
                ('shift', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_name', models.CharField(max_length=100)),
                ('readings', models.FloatField()),
                ('nominal', models.FloatField()),
                ('lsl', models.FloatField()),
                ('usl', models.FloatField()),
                ('status_cell', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('operator', models.CharField(max_length=100)),
                ('shift', models.CharField(max_length=100)),
                ('machine', models.CharField(max_length=100)),
                ('part_model', models.CharField(max_length=100)),
                ('part_status', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=100)),
                ('comp_sr_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='parameter_settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_id', models.CharField(max_length=255)),
                ('parameter_name', models.CharField(max_length=255)),
                ('sr_no', models.IntegerField()),
                ('single_radio', models.BooleanField(default=False)),
                ('analog_zero', models.FloatField(blank=True, null=True)),
                ('reference_value', models.FloatField(blank=True, null=True)),
                ('double_radio', models.BooleanField(default=False)),
                ('high_mv', models.FloatField(blank=True, null=True)),
                ('low_mv', models.FloatField(blank=True, null=True)),
                ('probe_no', models.FloatField()),
                ('measurement_mode', models.CharField(max_length=50)),
                ('nominal', models.FloatField()),
                ('usl', models.FloatField()),
                ('lsl', models.FloatField()),
                ('utl', models.FloatField()),
                ('ltl', models.FloatField()),
                ('job_dia', models.CharField(max_length=10)),
                ('digits', models.IntegerField()),
                ('mastering', models.FloatField()),
                ('step_no', models.FloatField()),
                ('hide_checkbox', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='parameterwise_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_model', models.CharField(max_length=100)),
                ('parameter_name', models.CharField(max_length=100)),
                ('operator', models.CharField(max_length=100)),
                ('formatted_from_date', models.CharField(max_length=100)),
                ('formatted_to_date', models.CharField(max_length=100)),
                ('machine', models.CharField(max_length=100)),
                ('vendor_code', models.CharField(max_length=100)),
                ('job_no', models.CharField(max_length=100)),
                ('shift', models.CharField(max_length=100)),
                ('current_date_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResetCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_model', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShiftSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(max_length=50)),
                ('shift_time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TableFiveData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TableFourData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator_no', models.CharField(max_length=100)),
                ('operator_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TableOneData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=100)),
                ('part_model', models.CharField(max_length=100)),
                ('part_no', models.CharField(max_length=100)),
                ('hide', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TableThreeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_no', models.CharField(max_length=100)),
                ('machine_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TableTwoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
