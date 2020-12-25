from django.urls import path

from p_library.views import AuthorCreate, AuthorDelete, AuthorRead, AuthorUpdate, friends_list


app_name = 'p_library'

urlpatterns = [
    path('author/create/', AuthorCreate.as_view(), name='author_create'),
    path('author/', AuthorRead.as_view(), name='author_read'),
    path('author/<int:pk>/', AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author_delete'),
    path('friend/', friends_list, name='friends')
]
