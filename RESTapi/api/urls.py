from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path("students/",views.students, name="students"),
    path("students/<int:student_id>/", views.student_detail, name="student_detail"),


    # path("employees/",views.Employees.as_view()),
    # path("employees/<int:pk>/", views.EmployeeDetail.as_view()),
    path("", include(router.urls)),


    path("blogs",views.Blogs.as_view()),
    path("blogs/<int:pk>",views.BlogDetail.as_view()),

    path("comments",views.Comments.as_view()),
    path("comments/<int:pk>",views.CommentDetail.as_view()),

]