from django.db import models

from pybb.models import Forum
from django.utils.translation import ugettext_lazy as _

class NewForum(Forum):
    promo_image = models.ImageField(upload_to='images/forums', blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    
    class Meta(object):
        ordering = ['position']
        verbose_name = _('NewForum')
        verbose_name_plural = _('NewForums')

    def __unicode__(self):
        return self.name

    def update_counters(self):
        self.post_count = Post.objects.filter(topic__forum=self).count()
        self.topic_count = Topic.objects.filter(forum=self).count()
        last_post = self.get_last_post()
        if last_post:
            self.updated = self.last_post.updated or self.last_post.created
        self.save()

    def get_absolute_url(self):
        return reverse('pybb:forum', kwargs={'pk': self.id})

    @property
    def posts(self):
        return Post.objects.filter(topic__forum=self).select_related()

    def get_last_post(self):
        try:
            return self.posts.order_by('-created').select_related()[0]
        except IndexError:
            return None

    @property
    def last_post(self):
        return self.get_last_post()

    def get_parents(self):
        """
        Used in templates for breadcrumb building
        """
        return self.category,