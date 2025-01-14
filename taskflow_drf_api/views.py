from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    """
    root_rout shows main message when page loads,
    taken from  code Institute moments react project.
    """
    return Response({
        "message": (
            "Welcome to taskFlow DRF API.",
            "At the end of the URL, type either: ",
            "- '/categories' ",
            "- '/tasks' ",
            "- '/task-files'",
            "to view the respective endpoints.",
        )
    })
