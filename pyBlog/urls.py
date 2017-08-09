from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', views.home, name='home'),
    url(r'^single-post/(?P<post_id>[0-9]+)/', views.single_post, name='single-post'),
    url(r'^cost/', include('cost.urls'), name="cost")
]
