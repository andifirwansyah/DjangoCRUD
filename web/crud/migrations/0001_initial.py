from __future__ import unicode_literals

from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
            ],
        ),
    ]
