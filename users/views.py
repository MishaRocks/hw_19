from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView


# Create your views here.
class LoginView(BaseLoginView):
    ...


class LogoutView(BaseLogoutView):
    ...
