from django.urls import path

from .views import (
        doctor_list,
        doctor_details,
        book_appoinment)


urlpatterns = [
    path('doctor_list/', doctor_list, name='doctor_list'),
    path('doctor_details/<int:id>/', doctor_details, name='doctor_details'),
    path('book_appoinment/<int:doctor_id>/', book_appoinment, name='book_appoinment'),
]