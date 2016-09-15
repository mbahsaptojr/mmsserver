# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apimms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donator',
            name='category',
            field=models.CharField(choices=[(b'i', b'individu'), (b'c', b'company')], default=2, max_length=1),
            preserve_default=False,
        ),
    ]
