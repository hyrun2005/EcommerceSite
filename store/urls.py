from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.home_page_view, name='home'),
    path("about/", views.about_page, name='about_page'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("register/", views.register_user, name="registrate"),
    path("product/<int:pk>/", views.product_info, name='product_info'),
    path("category/<str:foo>/", views.categories, name='categories'),
    path("cart/", include('cart.urls'))
]