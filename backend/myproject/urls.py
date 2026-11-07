from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

SMS_VERIFY_CONTENT = "محتوای دقیقی که sms.ir داده"

def sms_verify(request):
    return HttpResponse(SMS_VERIFY_CONTENT, content_type="text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sms-verify.txt', sms_verify),
    path('', include('landing.urls')),
]