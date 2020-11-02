from django.conf import settings
from django.urls import path, include, re_path
from django.contrib import admin
from core.views import IndexTemplateView


urlpatterns = [
    path("home/", IndexTemplateView, name="home"),
    #path('admin/', include('smuggler.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    # auth
    path("api-auth/", include("rest_framework.urls")),
    path("api/rest-auth/", include("rest_auth.urls")),
    path("api/rest-auth/registration/", include("rest_auth.registration.urls")),
    #####
    path("questions/", include("questions.api.urls")),
    path("users/", include("users.api.urls")),
    re_path(r"^.*$", IndexTemplateView, name="entry-point")
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),

    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
