
def test_is_app_logging_access(host):
    host.run('curl localhost:8000/?my-query-parameter')
    access_log = host.file('/var/log/my-app-access.log')
    assert access_log.exists
    assert access_log.contains('my-query-parameter')
