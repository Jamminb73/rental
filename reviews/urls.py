from django.urls import path

from . import views

urlpatterns = [
    path('', views.reviews, name="reviews"),
    path('create/', views.review_create, name="create"),
    path('<int:review_id>/', views.review_detail, name="detail"),
    path('update/<int:review_id>/', views.review_update, name='update'),
    path('delete/<int:review_id>/', views.review_delete, name='delete'),
]
