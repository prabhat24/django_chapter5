from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.home_view, name="home"),
    url(r'^about', views.about_us, name="about_us"),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.view_category, name='view_category'),
    url(r'^add_category/$', views.add_category,name="add_category"),
    url(r"^category/(?P<category_name_slug>[\w\-]+)/add_page/$", views.add_page, name= "add_page"),
]
