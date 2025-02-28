from collections import namedtuple
from urllib.parse import urlencode

from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView
from django_comparison_dashboard.models import Result

Model = namedtuple("Model", ("collection", "structure"))

MODELS = {
    "Overall System - Highest Level of Detail": Model("sedos-project", "SEDOS-structure-all"),
    "Overall System - Medium Level of Detail": Model("sedos-project", "SEDOS-structure-all-lod2"),
    "Overall System - Lowest Level of Detail": Model("sedos-project", "SEDOS-structure-all-lod1"),
    "Case Study - Steel Industry Section": Model("steel_industry_test", "SEDOS-structure-steel-industry-section"),
    "Case Study - Transport with Sector Coupling": Model("sedos-project", "SEDOS-structure-transport-sector-coupled"),
}

FORWARD_URLS = {
    "network": "django_energysystem_viewer:networks",
    "processes": "django_energysystem_viewer:processes",
    "artifacts": "django_energysystem_viewer:artifacts",
    "aggregations": "django_energysystem_viewer:aggregations",
}


class StartpageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        scenarios = Result.objects.exclude(
            name__in=[
                "io_groups",
                "ind_demo_online_v0",
                "ind_demo_online_v1",
                "ind_demo_online_v1",
                "t_all_tokio_v0",
                "t_all_tokio_v1 (t_all_tokio_v1.csv)",
                "t_all_tokio_v2 (t_all_tokio_v2.csv)",
                "o_steel_tokio (sedos_results.csv)",
                "t_all_tokio_v3 (t_all_tokio_v3.csv)",
                "f_tra_tokio (test_results.csv)",
            ]
        )
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
