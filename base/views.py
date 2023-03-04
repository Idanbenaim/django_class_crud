from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import serializers

from .models import Students

# Create your views here.

def index(r):
    return "hello"

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class manageStudents(APIView):
    """
    This class handle the CRUD operations for MyModel
    """
    
    def get(self, request, pk=-1):  # axios.get
        """
        Handle GET requests to return a list of MyModel objects
        """
        if pk > -1:
            my_model = Students.objects.get(id=pk)
            serializer = StudentsSerializer(my_model, many=False)
        else:
            my_model = Students.objects.all()
            serializer = StudentsSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):  # axios.post
        """
        Handle POST requests to create a new Task object
        """
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):  # axios.put
        """
        Handle PUT requests to update an existing Task object
        """
        my_model = Students.objects.get(pk=pk)
        serializer = StudentsSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # axios.delete
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = Students.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)