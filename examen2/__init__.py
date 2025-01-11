from .migratios import Movie


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            id='Movies',
            fields=[
                title = models.CharField(max_length=30, null=False)
    genre = models.CharField(max_length=30, null=False)
    director_name = models.CharField(max_length=30, null=False)
    publication_year = models.CharField(max_length=30, null=False)
    synopsis = models.TextField(null=False)
            ],
        ),
    ]
