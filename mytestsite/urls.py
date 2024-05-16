"""
URL configuration for locallibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# Use include() to add URLS from the catalog application and authentication system
from django.urls import include

# from rest_framework import permissions
# from drf_yasg2.views import get_schema_view
# from drf_yasg import openapi
# from drf_yasg2 import generators


urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
    path('catalog/', include('catalog.urls')),
]


# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Your API",
#         default_version="v1",
#         description="API documentation",
#         terms_of_service="https://localhost:8000",
#         # contact=openapi.Contact(email="your-contact-email@example.com"),
#         # license=openapi.License(name="Your License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

# urlpatterns += [
#     path("swagger/", schema_view.with_ui("swagger"), name="swagger"),
#     # path("redoc/", schema_view.with_ui("redoc"), name="redoc"),
#     # path("api/", include("your_app.urls")),
# ]