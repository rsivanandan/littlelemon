from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router: DefaultRouter = DefaultRouter()
router.register(r'booking', views.BookingViewSet) 

urlpatterns = [
    # Web Pages
    path('', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('menu/', views.menu_view, name='menu'),
    path('book/', views.book, name='book'),
    path('bookings/', views.get_bookings, name='bookings'), 
    path('reservations/', views.reservations, name="reservations"),
    # API paths
    path('api/menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item-api'),
    path('api/booking/', include(router.urls)),
    path('api/token-auth/', obtain_auth_token),
]