from django.shortcuts import render
import logging

logger = logging.getLogger('sourceDns.webdns.views')


def test(request):
    param = request.GET.get('name')
    # print param['age']
    logger.info('yangjiajia')
    try:
        if not isinstance(param, basestring):
            print 111111111111
    except Exception, e:
        print e
        logging.info('yangjiajia456789')
    return render(request, 'index.html')
# test(request='')


# Create your views here.
