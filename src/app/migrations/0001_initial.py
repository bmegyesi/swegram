# Generated by Django 4.0.5 on 2022-07-03 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_id', models.BigIntegerField(blank=True, null=True)),
                ('activated', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('lang', models.CharField(max_length=512)),
                ('filename', models.CharField(max_length=512)),
                ('file_size', models.CharField(max_length=512)),
                ('normalized', models.BooleanField(default=False)),
                ('parsed', models.BooleanField(default=False)),
                ('has_label', models.BooleanField(default=False)),
                ('labels', models.TextField(null=True)),
                ('number_of_paragraphs', models.IntegerField(blank=True, null=True)),
                ('number_of_sentences', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('md5_checksum', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('normalized', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general', models.TextField(null=True)),
                ('readability', models.TextField(null=True)),
                ('morph', models.TextField(null=True)),
                ('morph_average', models.TextField(null=True)),
                ('lexical', models.TextField(null=True)),
                ('lexical_average', models.TextField(null=True)),
                ('syntactic', models.TextField(null=True)),
                ('syntactic_average', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('stats', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.textstats')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general', models.TextField(null=True)),
                ('readability', models.TextField(null=True)),
                ('morph', models.TextField(null=True)),
                ('morph_average', models.TextField(null=True)),
                ('lexical', models.TextField(null=True)),
                ('lexical_average', models.TextField(null=True)),
                ('syntactic', models.TextField(null=True)),
                ('syntactic_average', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.text')),
            ],
        ),
    ]
