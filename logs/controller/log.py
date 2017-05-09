from django.shortcuts import *
import logging

logger = logging.getLogger('sourceDns.webdns.views')


def index(request):
    logger.info('success')
    return render(request, 'index.html')
