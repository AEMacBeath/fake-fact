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

        voted_fake = False
        if post.fake.filter(id=self.request.user.id).exists():
            voted_fake = True

        voted_fact = False
        if post.fact.filter(id=self.request.user.id).exists():
            voted_fact = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "messages": messages,
                "voted_fake": voted_fake,
                "voted_fact": voted_fact
            },
        )
