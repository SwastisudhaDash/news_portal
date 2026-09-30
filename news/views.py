from django.db.models import F, Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CommentForm
from .models import Article, Category

def home(request):
    published = Article.objects.filter(is_published=True)
    featured = published.filter(is_featured=True).first()
    breaking = published.filter(is_breaking=True)[:5]
    latest = published[:8]
    trending = published.order_by("-views", "-created_at")[:5]
    categories = Category.objects.all()
    return render(request, "home.html", {
        "featured": featured,
        "breaking": breaking,
        "latest": latest,
        "trending": trending,
        "categories": categories,
    })

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    Article.objects.filter(pk=article.pk).update(views=F("views") + 1)
    article.refresh_from_db()
    related = Article.objects.filter(
        category=article.category, is_published=True
    ).exclude(pk=article.pk)[:4]

    form = CommentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect(article.get_absolute_url())

    return render(request, "article_detail.html", {
        "article": article, "related": related, "form": form
    })

def category_news(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category, is_published=True)
    return render(request, "category.html", {"category": category, "articles": articles})

def search(request):
    query = request.GET.get("q", "").strip()
    articles = Article.objects.filter(is_published=True)
    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            Q(summary__icontains=query) |
            Q(content__icontains=query)
        )
    return render(request, "search.html", {"articles": articles, "query": query})
