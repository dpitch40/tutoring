def boolean_diff(l1, l2, transform=lambda x: x, sort=False):
    translated1 = dict(zip(map(transform, l1), l1))
    translated2 = dict(zip(map(transform, l2), l2))
    set1 = set(translated1.keys())
    set2 = set(translated2.keys())
    on1not2 = {translated1[f] for f in set1 - set2}
    on2not1 = {translated2[f] for f in set2 - set1}
    common = {translated1[f] for f in set1 & set2}
    if sort:
        return sorted(on1not2), sorted(common), sorted(on2not1)
    else:
        return on1not2, common, on2not1

def test_boolean_diff():
    l1 = ['a', 'b', 'c']
    l2 = ['a', 'b', 'd']
    assert boolean_diff(l1, l2) == ({'c'}, {'a', 'b'}, {'d'})
    assert boolean_diff(l1, l1) == (set(), {'a', 'b', 'c'}, set())

    l3 = ['a', 'B', 'd']
    assert boolean_diff(l1, l3) == ({'b', 'c'}, {'a'}, {'B', 'd'})
    assert boolean_diff(l1, l3, lambda x: x.lower()) == ({'c'}, {'a', 'b'}, {'d'})


# l1 = ['a', 'b']
# l2 = ['a', 'c']
# l1 - l2 = ['b']
