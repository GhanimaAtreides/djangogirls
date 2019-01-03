from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^experiments/experiment_exp_sum$', views.experiment_exp_sum, name='experiment_exp_sum'),
    url(r'^experiments/experiment_exp_sum.png', views.experiment_exp_sum_png, name='experiment_exp_sum_png')
]