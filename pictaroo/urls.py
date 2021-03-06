from django.conf.urls import url
from pictaroo import views
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name = 'about'),

    url(r'^add_category/$', views.add_category, name='add_category'),

    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),

    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_image/$',
        views.add_image, name='add_image'),

    url(r'^my_favourites/', views.my_favourites, name='my_favourites'),

    url(r'^my_comments/', views.my_comments, name='my_comments'),

    url(r'^my_uploads/', views.my_uploads, name='my_uploads'),

    url(r'^my_friends/', views.my_friends, name='my_friends'),

    url(r'^register_profile/$', views.register_profile, name='profile'),

    url(r'^my_account/(?P<username>[\w\-]+)/$', views.my_account, name='my_account'),

    url(r'^image_like/$', views.like_image, name='like_category'),

    url(r'^comment_like/$', views.like_comment, name='like_comment'),

]