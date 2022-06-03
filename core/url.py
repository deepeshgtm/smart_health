from django.urls import path, include
from .import views
from .api import *




urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('restricted/', views.restricted),
    path('api/doctors', DoctorApi.as_view()),
    path('api/create/doctor', DoctorCreateApi.as_view()),
    path('api/<int:pk>/update/doctor', DoctorUpdateApi.as_view()),
    path('api/<int:pk>/delete/doctor', DoctorDeleteApi.as_view()),
    path('api/patient', PatientApi.as_view()),
    path('api/create/patient', PatientCreateApi.as_view()),
    path('api/<int:pk>/update/patient', PatientUpdateApi.as_view()),
    path('api/<int:pk>/delete/patient', PatientDeleteApi.as_view()),
    path('api/blog', BlogApi.as_view()),
    path('api/create/blog', BlogCreateApi.as_view()),
    path('api/<int:pk>/update/blog', BlogUpdateApi.as_view()),
    path('api/<int:pk>/delete/blog', BlogDeleteApi.as_view()),
    path('api/appointment', AppointmentApi.as_view()),
    path('api/create/appointment', AppointmentCreateApi.as_view()),
    path('api/<int:pk>/update/appointment', AppointmentUpdateApi.as_view()),
    path('api/<int:pk>/delete/appointment', AppointmentDeleteApi.as_view()),
    path('api/query', QueryApi.as_view()),
    path('api/create/query', QueryCreateApi.as_view()),
    path('api/<int:pk>/update/query', QueryUpdateApi.as_view()),
    path('api/<int:pk>/delete/query', QueryDeleteApi.as_view()),
    path('api/medical_report', Medical_reportApi.as_view()),
    path('api/create/medical_report', Medical_reportCreateApi.as_view()),
    path('api/<int:pk>/update/medical_report', Medical_reportUpdateApi.as_view()),
    path('api/<int:pk>/delete/medical_report', Medical_reportDeleteApi.as_view()),

    # path('room/', views.room, name="room"),
    # path('room/access/<str:sid>/', views.token, name="token")
]