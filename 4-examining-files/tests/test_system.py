
def test_is_debian(host):
    assert host.system_info.distribution == 'debian'


def test_is_python_installed(host):
    result = host.run('python --version')
    assert result.rc == 0
    assert '3.5' in result.stdout
    result = host.run('pip --help')
    assert result.rc == 0


def test_are_python_web_stack_packages_installed(host):
    packages = host.pip_package.get_packages()
    assert 'Flask' in packages
    assert 'gunicorn' in packages


def test_does_my_app_user_exist_and_is_it_not_a_system_user(host):
    assert host.user('my-app').uid >= 1000
