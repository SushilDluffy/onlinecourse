# Generated by Django 3.1.6 on 2021-02-16 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500)),
                ('grade', models.IntegerField(default=0)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_content', models.CharField(max_length=200)),
                ('choice', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question')),
            ],
        ),
    ]
