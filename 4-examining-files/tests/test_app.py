
def test_app_is_running(host):
    host.run_expect((0,), 'curl localhost:8000')
    # ... or ...
    assert host.run('curl localhost:8000').rc == 0


def test_app_is_run_by_the_right_user(host):
    result = host.check_output('ps auxww | grep "/gunicorn"')
    first_proc = result.split("\n", 1)[1]
    assert first_proc.startswith('my-app')
