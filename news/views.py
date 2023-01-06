from django.shortcuts import render
from .models import News


# Create your views here.
def index(request):
    content_berita = News.objects.all()
    context = {
        "Content_Announ" : content_berita.filter(content_category="announcement"),
        "Content_Event" : content_berita.filter(content_category="incoming_event"),
        "Content_News" : content_berita.filter(content_category="hot_news"),
        "creator" : "Maulana Aji W.",
        "page_name" : "News",
        "site_nav" : [
            ["/", "Home"],
            ["/animelist", "Explorer"],
            ["/community", "Community"],
            ["/news", "News"],
            ["/user_profile", "Profile"],
        ],
        "website" : "My Anime List",
    }
    return render(request, "news/index.html", context)

def news_detail(request, slug):
    content_berita = News.objects.get(slug=slug)
    context = {
        "Contents" : content_berita,
        "page_name" : "News",
        "site_nav" : [
            ["/", "Home"],
            ["/animelist", "Explorer"],
            ["/community", "Community"],
            ["/news", "News"],
            ["/user_profile", "Profile"],
        ],
        "website" : "My Anime List",
    }
    return render(request, "news/news_detail.html", context)

# Note:
# Konten berita di dalam apps News terdapat 3 kategori yaitu:
# 1. incoming_event
# 2. hot_news
# 3. announcement
# keyboard error g, G, h, H, '_', "_"
