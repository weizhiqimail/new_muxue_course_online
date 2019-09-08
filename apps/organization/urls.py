from django.urls import path
from django.conf.urls import url

from organization.views import OrgView, AddAskView, OrgHomeView, OrgTeacherView, OrgCourseView, OrgDescView

urlpatterns = [
    path(r'list/', OrgView.as_view(), name="list"),
    path(r'add_ask/', AddAskView.as_view(), name="add_ask"),

    url(r'^(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="home"),
    url(r'^(?P<org_id>\d+)/teacher/$', OrgTeacherView.as_view(), name="teacher"),
    url(r'^(?P<org_id>\d+)/course/$', OrgCourseView.as_view(), name="course"),
    url(r'^(?P<org_id>\d+)/desc/$', OrgDescView.as_view(), name="desc"),

]
