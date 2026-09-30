from django.core.management.base import BaseCommand
from news.models import Category, Article

class Command(BaseCommand):
    help = "Create demo NewsHub content"

    def handle(self, *args, **options):
        names = ["National", "Odisha", "Technology", "Sports", "Business", "Entertainment"]
        cats = {name: Category.objects.get_or_create(name=name)[0] for name in names}
        demo = [
            ("Django NewsHub launches with a clean modern newsroom experience", "Technology", True, True),
            ("Odisha communities prepare for a new season of local events", "Odisha", False, False),
            ("New technology trends are changing how people read the news", "Technology", False, False),
            ("Weekend sports roundup: stories to follow this week", "Sports", False, False),
            ("Business desks watch the latest market developments", "Business", False, False),
            ("What readers are watching across entertainment today", "Entertainment", False, False),
        ]
        for title, category, featured, breaking in demo:
            Article.objects.get_or_create(
                title=title,
                defaults={
                    "category": cats[category],
                    "author": "NewsHub Desk",
                    "summary": "A sample NewsHub story created to demonstrate the portal layout and Django content workflow.",
                    "content": "This is demo content for the NewsHub portfolio project. Replace this article from the Django Admin with your own reporting, images and stories.",
                    "is_featured": featured,
                    "is_breaking": breaking,
                    "is_published": True,
                },
            )
        self.stdout.write(self.style.SUCCESS("Demo NewsHub content created."))
