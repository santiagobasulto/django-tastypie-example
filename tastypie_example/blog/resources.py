from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie_example.blog.models import Post


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'


class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
