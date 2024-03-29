# from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import (
    ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView,
)

from blog.models import Post


#-- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

# DetailView
class PostDV(DetailView):
    model = Post


# ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modified_at'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modified_at'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modified_at'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modified_at'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modified_at'


class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context









