from django.urls import path
from .views import SnackListView , SnackDetailView  ,SnackCreateView , SnackUpdateView ,SnackDeleteView

urlpatterns=[
    
    path('list',SnackListView.as_view(),name='snack_list'),
    path('list/<int:pk>',SnackDetailView.as_view(),name='snack_details'),
    path('snack/new',SnackCreateView.as_view(),name='create_snack'),
    path('list/<int:pk>/update', SnackUpdateView.as_view(),name="update_snack"),
    path('list/<int:pk>/delete', SnackDeleteView.as_view(),name="delete_snack")
]