from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(published=True).order_by('-created')
    template_name = 'index.html'
    paginate_by = 4


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(published=True)
        post = get_object_or_404(queryset, slug=slug)
        messages = post.messages.filter(accepted=True).order_by('received')

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "messages": messages
            },
        )
