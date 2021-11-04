# Generated by Django 3.2.8 on 2021-10-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('locality', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Khulna', 'Khulna'), ('Rajshahi', 'Rajshahi'), ('Barisal', 'Barisal'), ('Sylhet', 'Sylhet'), ('Chattogram', 'Chattogram'), ('Rangpur', 'Rangpur')], max_length=30)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('job_city', models.CharField(max_length=30)),
                ('profile_image', models.ImageField(blank=True, upload_to='profileImg')),
                ('my_file', models.FileField(blank=True, upload_to='doc')),
            ],
        ),
    ]
