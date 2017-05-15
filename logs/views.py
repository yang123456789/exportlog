from django.shortcuts import render
import logging
import json
import requests

# url = 'http://192.168.219.201:8080/v2/apps/{0}'

logger = logging.getLogger('sourceDns.webdns.views')


def test(request):
    # urls = url.format('yang')
    # param = {
    #     'id': 'yang',
    #     'cpus': 0.6,
    #     'mem': 128,
    #     'disk': 0,
    #     'instances': 1
    # }
    # data = json.dumps(param)
    #
    # try:
    #     requests.put(urls, data)
    # except Exception, e:
    #     print e
    #     logging.exception(e)
    return render(request, 'index.html')
# test(request='')


# Create your views here.
