# -*- encoding:utf-8 -*-
# !/usr/bin/env python3
from collections import namedtuple
from collections import deque
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
#collections
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p.x
isinstance(p, Point)
#deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')

#defaultdict
dd = defaultdict(lambda: 'N/A')

#OrderedDict
#插入的顺序排序而不是key的顺序
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

#Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1