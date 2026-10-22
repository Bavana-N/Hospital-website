from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.Home, name='home'),
    path('service/<int:id>/', views.Cardiology, name='cardiology'),
    path('BookAppointment/<int:id>/',views.BookAppointment,name='book_appo1'),
    # path('Book/',views.Book,name='book'),
    path('logout/',views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )