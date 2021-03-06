# Generated by Django 2.2.7 on 2021-01-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210105_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='文章分类', max_length=128, verbose_name='文章分类')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='文章标签', max_length=128, verbose_name='文章标签')),
            ],
        ),
        migrations.AlterField(
            model_name='articles',
            name='visited',
            field=models.IntegerField(verbose_name='文章访问量'),
        ),
        migrations.AddField(
            model_name='articles',
            name='Tag',
            field=models.ManyToManyField(to='articles.Tag', verbose_name='文章标签'),
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ManyToManyField(to='articles.Category', verbose_name='文章分类'),
        ),
    ]
