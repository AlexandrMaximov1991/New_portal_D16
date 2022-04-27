import pytz
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import *
from .models import *
from .filters import News_filter
from .forms import PostForm
from django.utils.translation import gettext as _


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 1
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = News_filter(self.request.GET, queryset=self.get_queryset())
        return context

    def __str__(self):
        return f'{self.PostAuthor}'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        categories = []
        post = Post.objects.get(pk=id)
        for cat in post.postCategory.all():
            if self.request.user in cat.subscribers.all():
                categories.append(cat)
        context['user_category'] = categories
        return context


class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('news_portal.add_post',)
    template_name = 'post_create.html'
    form_class = PostForm


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'post_create.html'
    permission_required = ('news_portal.change_post',)
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'post_delete.html'
    permission_required = ''
    queryset = Post.objects.all()
    success_url = '/news/'


class Postsearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = News_filter(self.request.GET, queryset=self.get_queryset())
        return context


@login_required
def subscribe(request, **kwargs):
    user = request.user
    cat_id = kwargs['pk']
    category = Category.objects.get(pk=int(cat_id))

    if user not in category.subscribers.all():
        category.subscribers.add(user)

    else:
        category.subscribers.remove(user)

    return redirect(request.META.get('HTTP_REFERER', '/'))


class Index(View):
    def get(self, request):
        curent_time = timezone.now()

        # .  Translators: This message appears on the home page only
        models = Post.objects.all()

        context = {
            'models': models,
            'current_time': timezone.now(),
            'timezones': pytz.common_timezones  # добавляем в контекст все доступные часовые пояса
        }

        return HttpResponse(render(request, 'news.html', context))

    #  по пост-запросу будем добавлять в сессию часовой пояс, который и будет обрабатываться написанным нами ранее middleware
    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')

# def set_timezone(request):
#     if request.method == 'POST':
#         request.session['django_timezone'] = request.POST['timezone']
#         return redirect('/')
#     else:
#         return render(request, 'news.html', {'timezones': pytz.common_timezones})