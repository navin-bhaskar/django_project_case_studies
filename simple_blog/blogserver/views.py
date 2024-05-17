import json
from django.http import JsonResponse

# Create your views here.
from .models import BlogPost


def home(request):
    if request.method == "GET":
        posts = get_posts()
        return JsonResponse({"posts": posts})
    if request.method == "POST":
        post_data = json.loads(request.body)
        save_blog_post(
            post_data["title"], post_data["description"], post_data["created_by"]
        )

    return JsonResponse({"message": "Post added successfully"})


def save_blog_post(title, description, created_by):
    blog_post = BlogPost(title=title, description=description, created_by=created_by)
    blog_post.save()
    return blog_post


def get_posts():
    all_posts = []

    for post in BlogPost.objects.all():
        all_posts.append(
            {
                "title": post.title,
                "description": post.description,
                "created_by": post.created_by,
                "created_at": str(post.created_at),
            }
        )

    return all_posts
