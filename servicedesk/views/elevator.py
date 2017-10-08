from django.contrib.auth.decorators import permission_required
from servicedesk.models import Elevator

from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView


# @method_decorator(permission_required('servicedesk.service_desk', raise_exception=True), name='dispatch')
class ElevatorListView(TemplateView):
    template_name = 'elevator/elevators.html'

    def get_context_data(self, **kwargs):
        context = super(ElevatorListView, self).get_context_data(**kwargs)
        context['elevators'] = Elevator.objects.all()
        #Elevator.address.
        return context


class ElevatorDetailView(DetailView):

    model = Elevator
    template_name = 'elevator/elevator_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return context
