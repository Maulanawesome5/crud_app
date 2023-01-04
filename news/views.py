from django.shortcuts import render
from .models import News


# Create your views here.
def index(request):
    content_berita = News.objects.all()
    context = {
        "Content_Event" : content_berita.filter(content_category="incoming_event"),
        "Content_News" : content_berita.filter(content_category="hot_news"),
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
    return render(request, "index.html", context)

# Note:
# Konten berita di dalam apps News terdapat 3 kategori yaitu:
# 1. incoming_event
# 2. hot_news
# 3. announcement
