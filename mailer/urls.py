from django.conf.urls import url
from django.contrib import admin
from main.views import SendMailView, ReactView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^send_mail/$', SendMailView.as_view()),
    url(r'^.*', ReactView.as_view())
]
