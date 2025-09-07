# closetmuse/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "users": reverse("user-list", request=request, format=format),
        "wardrobe": reverse("wardrobe-list", request=request, format=format),
        "planner": reverse("planner-list", request=request, format=format),
        "declutter": reverse("declutter-list", request=request, format=format),
    })
