from utils.serializers.fury_util import FuryUtil
from utils.serializers.cloud_pickle_util import CloudPickleUtil
from test_class.simple_class import SimpleClass


def get_test_class():
    s = SimpleClass()
    s.f2 = {"k1": "v1", "k2": "v2"}
    s.f1, s.f3 = s, s.f2
    s.f2['k2'] = 'v2_v2'
    s.f4.append('a')
    s.f4.append('b')
    s.f4.append('c')
    s.f5.append('a')
    s.f5.append('b')
    s.f5.append('c')
    s.f6.put(1)
    s.f6.put('c')

    return s


def test_fury():
    fury_util = FuryUtil()

    s = get_test_class()

    data = fury_util.serialize(s)
    s1 = fury_util.deserialize(data)
    print(s1.f1)
    print(s1.f2)
    print(s1.f3)
    print(s1.f4)
    print(s1.f5)
    print(s1.f6)

    setattr(s1, 'not_empty', True)
    print(getattr(s1, 'not_empty'))
    print(s1.f6.get(0))
    print(s1.f6.get(1))
    print(s1.f6)
    print(s1.f6.get(0))
    print(s1.f6.get(1))



def test_cloud_pickle():
    c = CloudPickleUtil()
    s = get_test_class()
    print(s.f6.qsize())
    data = c.serialize(s)
    s1 = c.deserialize(data)
    print(s1.f1)
    print(s1.f2)
    print(s1.f3)
    print(s1.f4)
    print(s1.f5)
    print(s1.f6)
    print(s1.f6.qsize())
    print(s1.f6.queue)
    print(s1.f6.get(0))
    print(s1.f6.get(1))



def test_get_set_state():
    s = get_test_class()
    state = {'a': 'a', 'b': 'b'}
    s.__setstate__(state)
    print(s.__getstate__())


if __name__ == '__main__':

    # fury 复杂类要注册
    # test_fury()
    test_cloud_pickle()

    # test_get_set_state()

