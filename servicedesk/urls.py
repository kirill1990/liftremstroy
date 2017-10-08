from django.conf.urls import url

from servicedesk.views import DeskView
from servicedesk.views import ElevatorListView, ElevatorDetailView

urlpatterns = [
    url(r'list', DeskView.as_view(), name='list'),

    url(r'elevators$', ElevatorListView.as_view(), name='elevators'),
    url(r'elevators/(?P<pk>[0-9]+)/$', ElevatorDetailView.as_view(), name='elevator-detail'),
]
