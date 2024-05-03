from django.urls import path

from accounts.views import SignUpView, EditarPerfil, DetallePerfil


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", DetallePerfil.as_view(), name="profile-detail"),
    path("profile/update/", EditarPerfil.as_view(), name="profile-update"),
]