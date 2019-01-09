from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

class Blocker(MiddlewareMixin):
    # Check if client IP is allowed
    def process_request(self, request):
        blocker_ips = ['0.0.0.1']
        ip = request.META.get('REMOTE_ADDR')
        if ip in blocker_ips:
            return HttpResponseForbidden()
        return None