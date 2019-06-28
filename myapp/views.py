from django.views.generic import TemplateView
from myapp.models import MyModel
from myapp.tasks import counter


class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance_counter = 0
        if MyModel.objects.exists():
            instance_counter = MyModel.objects.get(id=1).counter
        context['counter'] = instance_counter
        counter.delay()
        return context
