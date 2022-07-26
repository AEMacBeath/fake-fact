from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView

from .models import Post, Message
from .forms import MessageForm


# Post list view
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(published=True).order_by('-created')
    template_name = 'index.html'
    paginate_by = 4


# Fake vote view
class PostFakeVote(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.fake.filter(id=request.user.id).exists():
            post.fake.remove(request.user)
        else:
            post.fake.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Fact vote view
class PostFactVote(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.fact.filter(id=request.user.id).exists():
            post.fact.remove(request.user)
        else:
            post.fact.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Post detial view
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(published=True)
        post = get_object_or_404(queryset, slug=slug)
        messages = post.messages.filter(accepted=True).order_by('received')
        all_messages = post.messages.order_by('received')

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
                "all_messages": all_messages,
                "messaged": False,
                "voted_fake": voted_fake,
                "voted_fact": voted_fact,
                "message_form": MessageForm
            },
        )


# Create Messages
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(published=True)
        post = get_object_or_404(queryset, slug=slug)
        messages = post.messages.filter(accepted=True).order_by("received")

        voted_fake = False
        if post.fake.filter(id=self.request.user.id).exists():
            voted_fake = True

        voted_fact = False
        if post.fact.filter(id=self.request.user.id).exists():
            voted_fact = True

        message_form = MessageForm(data=request.POST)
        if message_form.is_valid():
            message_form.instance.author = request.user
            message = message_form.save(commit=False)
            message.post = post
            message.save()
        else:
            message_form = MessageForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "messages": messages,
                "message_form": message_form,
                "messaged": True,
                "voted_fake": voted_fake,
                "voted_fact": voted_fact
            },
        )


# Update Message
class MessageUpdateView(UpdateView):
    model = Message
    template_name = 'message_update.html'
    fields = ['body', ]
    form = MessageForm

    def get_success_url(self):
        post = self.object.post
        return reverse_lazy('post_detail', kwargs={'slug': post.slug})


# Delete Message
class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_delete.html'

    def get_success_url(self):
        post = self.object.post
        return reverse_lazy('post_detail', kwargs={'slug': post.slug})
