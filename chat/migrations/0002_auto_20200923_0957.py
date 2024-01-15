# Generated by Django 3.0.7 on 2020-09-23 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='chat.Full_chat')),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
