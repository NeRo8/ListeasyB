from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfilesSerializer
from .models import Profile


@api_view(['GET', 'PUT', 'DELETE'])
def profile_detail(request):
    """
    Retrieve, update or delete a code profie.
    """
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfilesSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfilesSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)