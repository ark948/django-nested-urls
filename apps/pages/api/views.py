from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_index(request):
    return Response(
        {
            "message": "welcome to index of pages api",
        }
    )