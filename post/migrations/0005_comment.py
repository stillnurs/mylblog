# Generated by Django 3.1 on 2020-08-19 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200818_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.post')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Коментарии',
                'ordering': ['-created'],
            },
        ),
    ]
