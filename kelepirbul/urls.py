
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from madde import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('madde.urls')),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.registration, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
