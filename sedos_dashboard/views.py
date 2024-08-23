from urllib.parse import urlencode

from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView
from django_comparison_dashboard.models import Result


class StartpageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        scenarios = Result.objects.all()
        return {"scenarios": scenarios}

    def get(self, request, *args, **kwargs):
        if "diagrams" in request.GET:
            base_url = reverse("django_comparison_dashboard:dashboard")
            query_string = urlencode(request.GET)
            url = f"{base_url}?{query_string}"
            return redirect(url)
        return super().get(request, *args, **kwargs)
