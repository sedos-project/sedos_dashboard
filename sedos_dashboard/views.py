from collections import namedtuple
from urllib.parse import urlencode

from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView
from django_comparison_dashboard.models import Result

Model = namedtuple("Model", ("collection", "structure"))

MODELS = {"Stahlindustrie": Model("steel_industry_test", "SEDOS-structure-steel_industry")}

FORWARD_URLS = {
    "network": "django_energysystem_viewer:networks",
    "processes": "django_energysystem_viewer:processes",
    "artifacts": "django_energysystem_viewer:artifacts",
    "aggregations": "django_energysystem_viewer:aggregations",
}


class StartpageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        scenarios = Result.objects.all()
        return {"scenarios": scenarios, "models": MODELS.keys()}

    def get(self, request, *args, **kwargs):
        if "diagrams" in request.GET:
            base_url = reverse("django_comparison_dashboard:dashboard")
            query_string = urlencode(request.GET)
            url = f"{base_url}?{query_string}"
            return redirect(url)
        for target in FORWARD_URLS:
            if target in request.GET:
                base_url = reverse(FORWARD_URLS[target])
                model = request.GET["model"]
                collection = MODELS[model].collection
                structure = MODELS[model].structure
                url = f"{base_url}?collection={collection}&structure={structure}"
                return redirect(url)
        return super().get(request, *args, **kwargs)
