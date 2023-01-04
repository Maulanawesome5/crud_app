from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "page_name" : "Explore",
        "site_nav" : [
            ["/", "Home"],
            ["/animelist", "Explorer"],
            ["/community", "Community"],
            ["/news", "News"],
            ["/user_profile", "Profile"],
        ],
        "website" : "My Anime List",
    }
    return render(request, "animelist/index.html", context)
