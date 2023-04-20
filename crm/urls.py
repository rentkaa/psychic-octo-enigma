from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from django.urls import include
from leads.views import landing_page, LandingPageView
from django.contrib.auth.views import LoginView, LogoutView,PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from leads.views import SignupView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LandingPageView.as_view(), name='landing-page'),
    path('leads/', include('leads.urls', namespace = "leads")),
    path('agents/', include('agents.urls', namespace = "agents")),
    path('signup/', SignupView.as_view(), name="signup"),
    path('reset-password/', PasswordResetView.as_view(), name="reset-password"),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('login/', LoginView.as_view(), name= "login"),
    path('logout/', LogoutView.as_view(), name= "logout")
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
