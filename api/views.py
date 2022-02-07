from .models import Employee
from .serializers import EmployeeSerializer 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.customauth import CustomAuthentication

class EmployeeModelViewSet(viewsets.ModelViewSet):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer
	authentication_class=[CustomAuthentication]
	# permission_classes=[IsAuthenticated]