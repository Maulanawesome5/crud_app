from django.shortcuts import render
from news.models import News


def index(request):
    content_berita = News.objects.all()
    context = {
        "app_css" : "css/styles.css",
        "Content_Announ" : content_berita.filter(content_category="announcement"),
        "Content_Event" : content_berita.filter(content_category="incoming_event"),
        "Content_News" : content_berita.filter(content_category="hot_news"),
        "creator" : "Maulana Aji W.",
        "page_name" : "Home",
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
