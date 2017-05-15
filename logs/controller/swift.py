# coding: utf-8

import swiftclient

_authurl = 'http://swift.sspaas.net:5000/v3/'
_auth_version = '3'
_user = 'docker'
_key = 'RSRZrcj@1233'
_os_options = {
    'user_domain_name': 'Default',
    'project_domain_name': 'Default',
    'project_name': 'docker'
}

conn = swiftclient.Connection(
    authurl=_authurl,
    user=_user,
    key=_key,
    os_options=_os_options,
    auth_version=_auth_version
)


# create object
# container = 'docker_log'
# conn.put_object(container, 'a.txt', contents='asdfasdfadfs', content_type='text/plain')


# Download 1
# http://swift.sspaas.net:8080/v1/AUTH_b070254add9b47738f85eb5ca9ecc7eb/docker_log/文件名
#
# Download 2
# obj = 'a.txt'
# resp_headers, obj_contents = conn.get_object(container, obj)
# with open('/root/aaaaaa.txt', 'w') as local:
#     local.write(obj_contents)
#

# delete
# obj = 'a.txt'
# container = 'docker_log'
# conn.delete_object(container, obj)
