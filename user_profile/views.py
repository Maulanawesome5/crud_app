from django.shortcuts import render
from .forms import Form_Register


# Create your views here.
def index(request):
    register_forms = Form_Register()
    context = {
        "creator" : "Maulana Aji W.",
        "page_name" : "User Profile",
        "register_forms" : register_forms,
        "site_nav" : [
            ["/", "Home"],
            ["/animelist", "Explorer"],
            ["/community", "Community"],
            ["/news", "News"],
            ["/user_profile", "Profile"],
        ],
        "website" : "My Anime List",
    }
    print(request.POST)
    return render(request, "user_profile/index.html", context)
