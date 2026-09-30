from django.db import migrations, models
import django.db.models.deletion
import django.utils.text

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=80, unique=True)),
                ("slug", models.SlugField(blank=True, max_length=90, unique=True)),
            ],
            options={"ordering": ["name"], "verbose_name_plural": "Categories"},
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=220)),
                ("slug", models.SlugField(blank=True, max_length=240, unique=True)),
                ("author", models.CharField(default="NewsHub Desk", max_length=100)),
                ("summary", models.TextField(max_length=400)),
                ("content", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="articles/")),
                ("is_featured", models.BooleanField(default=False)),
                ("is_breaking", models.BooleanField(default=False)),
                ("is_published", models.BooleanField(default=True)),
                ("views", models.PositiveIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="articles", to="news.category")),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=80)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField(max_length=500)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("article", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="comments", to="news.article")),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
