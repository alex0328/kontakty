from django.urls import path
from contacts import views


app_name = 'contacts'
urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
    path('delete/<int:pk>', views.DeleteUserView.as_view(), name='delete'),
    path('edit/<int:pk>', views.EditUserView.as_view(), name='edit'),
    path('details/<int:pk>', views.DetailsUserView.as_view(), name='details'),
]
