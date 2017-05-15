from logs.views import *

logger = logging.getLogger('sourceDns.webdns.views')

url = 'http://192.168.219.201:8080/v2/apps/{0}'


def index(request):
    urls = url.format('yang')
    param = {
        'id': 'yang',
        'cpus': 0.6,
        'mem': 128,
        'disk': 0,
        'instances': 1
    }
    data = json.dumps(param)
    print requests.put(urls, data)
    try:
        req = requests.put(urls, data)
        print req
    except Exception, e:
        print e
        logging.exception(e)
    return render(request, 'index.html')
# test(request='')
from django.http import StreamingHttpResponse


def generate_log(request):
    param = request.GET
    file_name = param.get('file_name')
    data = '12312313132231213123131321313211231311'
    with open(file_name, 'w') as f:
        f.write(data)
    return True


def downloads_log(request):
    print request.GET
    def file_iter(file_name, chunk_size=128):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                break
    the_file_name = 'yang.log'
    response = StreamingHttpResponse(file_iter(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename={0}'.format(the_file_name)
    return response
