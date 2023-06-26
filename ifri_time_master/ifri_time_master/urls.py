"""
URL configuration for ifri_time_master project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inscription.views import inscription, connexion, index, Contact, forgot, dashboard, deconnexion, dashboard
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription/', inscription, name='inscription'),
    path('connexion/', connexion, name='connexion'),
    path('', index, name='index'),
    path('contact/', Contact, name='contact'),
    path('forgot/', forgot, name='forgot'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    path('dashboard/', dashboard, name='dashboard'),
    # mot de passe oublie
    path('reset_password', views.PasswordResetView.as_view(
        template_name='forgot.html'), name="reset_password"),
    path('reset_password_send', views.PasswordResetDoneView.as_view(
        template_name='forgot_send.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(
        template_name='forgot_reset.html'), name="password_reset_confirm"),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(
        template_name='forgot_done.html'), name="password_reset_complete")

]
