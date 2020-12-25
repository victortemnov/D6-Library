from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from p_library import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls')),
    path('', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('publishers/', views.publishers_list),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)