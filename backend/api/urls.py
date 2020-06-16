from django.urls import path
from .views import AssignmentList, AssignmentDetail
from .views import BookList, BookDetail

urlpatterns = [
    # Assignments Application - API Control Routes
    path('assignments/', AssignmentList.as_view()),
    path('assignments/<int:pk>/', AssignmentDetail.as_view())
]

urlpatterns += [
    # Books Application - API Control Routes
    path('books/', AssignmentList.as_view()),
    path('books/<int:pk>/', AssignmentDetail.as_view())  
]