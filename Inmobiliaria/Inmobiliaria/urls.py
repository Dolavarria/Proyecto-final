from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from Arriendos.views import register, CustomLoginView, profile, update_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('accounts/profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
]