from django.conf.urls import url
from django.contrib import admin
import face_detector.views

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^face_detection/detect/$', face_detector.views.detect),
]
