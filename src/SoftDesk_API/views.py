from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'message': "Bienvenue sur l'API SoftDesk",
        # Vous pouvez ajouter ici des liens vers d'autres endpoints. Pertinent ?
    })
