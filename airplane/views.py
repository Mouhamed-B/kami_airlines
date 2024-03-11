from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Airplane
from .serializers import AirplaneSerializer

# Create your views here.

class AirplaneViewSet(viewsets.ModelViewSet):
    """
    API endpoints that to manage airplanes.
    """
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    """
    custom method to create single airplane
    """
    def create_object(self, data):
        serializer:AirplaneSerializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)   
        serializer.save()
        return serializer.data

    """
    override create method from super class to handle multiple airplanes input
    """
    def create(self, request, *args, **kwargs):
        if(isinstance(request.data,dict)):
            data:Airplane = self.create_object(request.data)
        elif (isinstance(request.data,list)):
            data:list = list()
            for object in request.data:
                data.append(self.create_object(object))
          # Saves all validated objects
        return Response(data, status=status.HTTP_201_CREATED)