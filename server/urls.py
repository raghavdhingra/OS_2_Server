"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views as mainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainView.portfolio, name="portfolio"),
    path('projects', mainView.projects, name="projects"),
    path('blogs', mainView.blogs, name="blogs"),
    path('submitForm', mainView.submitForm, name="submitForm"),
    path('whatsapp', mainView.whatsapp, name="whatsapp"),
    path('facebook', mainView.facebook, name="facebook"),
    path('twitter', mainView.twitter, name="twitter"),
    path('linkedin', mainView.linkedin, name="linkedin"),
    path('github', mainView.github, name="github"),
    path('codepen', mainView.codepen, name="codepen"),
    path('instagram', mainView.instagram, name="instagram"),
    path('telegram', mainView.telegram, name="telegram"),
    path('medium', mainView.medium, name="medium"),
    path('mail', mainView.mail, name="mail"),
    path('email', mainView.mail, name="email"),
    path('phone', mainView.mobile, name="phone"),
    path('message', mainView.mobile, name="message"),
    path('mobile', mainView.mobile, name="mobile"),
    # path('api/v1/projects', mainView.AllProjects.as_view()),
    # path('api/v1/testimonials', mainView.AllTestimonials.as_view()),
    path('dsc-mail', mainView.DscForm.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)