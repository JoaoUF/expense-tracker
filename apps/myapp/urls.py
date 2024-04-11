from django.urls import path
from apps.myapp import views

urlpatterns = [
    path('post/', views.ExpenseList.as_view()),
    path('post/<uuid:pk>/', views.ExpenseDetail.as_view()),
]
