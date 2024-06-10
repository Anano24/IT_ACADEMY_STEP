from django.urls import path
from . import views



app_name = 'blogapp'


urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('blog_detail/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('add_blog', views.AddBlogView.as_view(), name='add_blog'),
    path('delete_blog/<int:pk>', views.DeleteBlogView.as_view(), name='delete_blog'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('sign_up/', views.UserSignUpView.as_view(), name='sign_up')
]