from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^first_app/', include('apps.first_app.urls')),
    url(r'^time_display/', include('apps.time_display.urls')),
    url(r'^rand_word/', include('apps.rand_word.urls')),
    url(r'^survey_form/', include('apps.survey_form.urls')),
    url(r'^session_words/', include('apps.session_words.urls')),
    url(r'^amadon/', include('apps.amadon.urls')),
    url(r'^ninja_gold/', include('apps.ninja_gold.urls')),
    url(r'^user_login/', include('apps.user_login.urls')),
    url(r'^dojo_ninjas/', include('apps.dojo_ninjas.urls')),
    url(r'^rest_users/', include('apps.rest_users.urls')),
    url(r'^courses/', include('apps.courses.urls')),
    # url(r'^admin/', admin.site.urls)
]