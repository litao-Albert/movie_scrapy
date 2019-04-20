from django.shortcuts import render_to_response
from AritcleBlog.Article.models import Article

def index(request):
    # articles = Article.ob
    return render_to_response("newslistpic.html",locals())

# Create your views here.
