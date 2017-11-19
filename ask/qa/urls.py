from __future__ import unicode_literals

from django.conf.urls import include, url

from views import test, question_view, popular, question_list

urlpatterns = [
    url(r'question/(?P<question_id>[0-9]+)$', question_view),
    url(r'popular/$', popular),
    url(r'$', question_list),
    url(r'ask/', test),
    url(r'popular/', test),
    url(r'new/', test),
]
