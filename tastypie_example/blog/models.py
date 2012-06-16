from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1500)
    pub_date = models.DateTimeField('date published',
                    auto_now=False, auto_now_add=True)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.user)
