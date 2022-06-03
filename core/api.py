from rest_framework import generics
from rest_framework.response import Response
from .serializer import DoctorSerializer, UserSerializer, BlogSerializer, AppointmentSerializer, QuerySerializer, Medical_reportSerializer
from .models import Doctor, Patient, Blog, Appointment, Query, Medical_report


class DoctorCreateApi(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorApi(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDeleteApi(generics.DestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientCreateApi(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = UserSerializer


class PatientApi(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = UserSerializer


class PatientUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = UserSerializer


class PatientDeleteApi(generics.DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = UserSerializer


class BlogCreateApi(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogApi(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDeleteApi(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class AppointmentCreateApi(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentApi(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentDeleteApi(generics.DestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class QueryCreateApi(generics.CreateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class QueryApi(generics.ListAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class QueryUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class QueryDeleteApi(generics.DestroyAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

class Medical_reportCreateApi(generics.CreateAPIView):
    queryset = Medical_report.objects.all()
    serializer_class = Medical_reportSerializer


class Medical_reportApi(generics.ListAPIView):
    queryset = Medical_report.objects.all()
    serializer_class = Medical_reportSerializer


class Medical_reportUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Medical_report.objects.all()
    serializer_class = Medical_reportSerializer


class Medical_reportDeleteApi(generics.DestroyAPIView):
    queryset = Medical_report.objects.all()
    serializer_class = Medical_reportSerializer