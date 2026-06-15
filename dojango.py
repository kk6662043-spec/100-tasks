from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='secret',
    ALLOWED_HOSTS=['*'],
)

def home(request):
    return HttpResponse("""
    <h1>Welcome to My Django Homepage</h1>
    <p>Hello from Django!</p>
    """)

urlpatterns = [
    path('', home),
]

if __name__ == "__main__":
    execute_from_command_line(["manage.py", "runserver"])