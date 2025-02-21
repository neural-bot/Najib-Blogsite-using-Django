from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home_page_posts, name='home_page_posts'),
    path('post/<int:id>/', views.post_details, name='post_details'),
    path('create/', views.create_post, name='create_post'),
    path('post/update/<int:id>/', views.update_post, name='update_post'),
    path('post/delete/<int:id>/', views.delete_post, name='delete_post'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)