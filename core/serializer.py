from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.serializers import Serializer, FileField
from rest_framework import serializers
from .models import *


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Users
        fields = ('id', 'email', 'user_name', 'password', 'first_name', 'last_name', 'phone')


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'

class Medical_reportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical_report
        fields = '__all__'

