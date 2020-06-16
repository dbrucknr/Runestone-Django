from django.urls import path
from .views import AssignmentList, AssignmentDetail
from .views import BookList, BookDetail
from .views import UserList, UserDetail
from .views import CourseList, CourseDetail

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

urlpatterns += [
    # Users Application - API Control Routes
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns += [
    path('courses/', CourseList.as_view()),
    path('courses/<int:pk>/', CourseDetail.as_view())
]