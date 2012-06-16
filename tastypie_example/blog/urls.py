from django.conf.urls import patterns, include, url

from tastypie.api import Api
from tastypie_example.blog.resources import PostResource, UserResource

post_resource = PostResource()


urlpatterns = patterns('',

)
