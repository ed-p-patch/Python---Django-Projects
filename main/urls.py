from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^first_app/', include('apps.first_app.urls')),
    url(r'^time_display/', include('apps.time_display.urls')),
    url(r'^rand_word/', include('apps.rand_word.urls')),
    url(r'^survey_form/', include('apps.survey_form.urls')),
    url(r'^session_words/', include('apps.session_words.urls')),
    url(r'^amadon/', include('apps.amadon.urls')),
    # url(r'^admin/', admin.site.urls)
]