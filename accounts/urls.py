from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from accounts.views import home, createStudent, createTeacher, userdetails
app_name = 'accounts' # for namespacing

# urls  
urlpatterns = [
    path('', home, name='home'),
    path('signup/', include(([
        path('student', createStudent, name='createStudent'),
        path('teacher', createTeacher, name='createTeacher'),
])),),
    path('deets/<pk>', userdetails.as_view(), name='details'), # user detail from class view
    # using django default login and logout views
    path('login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
