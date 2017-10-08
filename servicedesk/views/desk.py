from django.contrib.auth.decorators import permission_required
from servicedesk.models import Incident

from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(permission_required('servicedesk.service_desk', raise_exception=True), name='dispatch')
class DeskView(TemplateView):
    template_name = 'desk.html'

    def get_context_data(self, **kwargs):
        context = super(DeskView, self).get_context_data(**kwargs)

        context['incidents'] = Incident.objects.all()

        return context
