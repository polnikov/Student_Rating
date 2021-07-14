from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', include('main.urls')),
    path('students/', include('student.urls', namespace='students')),
    path('subjects/', include('subject.urls',namespace='subjects')),
# TODO:     path('statistics/', include('statistics.urls')),
# TODO:     path('money/', include('money.urls')),
# TODO:     path('arrear/', include('arrear.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

