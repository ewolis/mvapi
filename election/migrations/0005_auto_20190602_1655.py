# Generated by Django 2.2.1 on 2019-06-02 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0004_auto_20190521_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='mentions_by_candidate',
            new_name='grades_by_candidate',
        ),
    ]