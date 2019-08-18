from django.urls import path
from contacts import views
from django.conf.urls.static import static
from django.conf import settings



app_name = 'contacts'
urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
    path('delete/<int:pk>', views.DeleteUserView.as_view(), name='delete'),
    path('edit/<int:pk>', views.EditUserView.as_view(), name='edit'),
    path('details/<int:pk>', views.DetailsUserView.as_view(), name='details'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
