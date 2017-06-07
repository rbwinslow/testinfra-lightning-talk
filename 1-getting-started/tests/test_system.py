
def test_is_debian(host):
    assert host.system_info.distribution == 'debian'
