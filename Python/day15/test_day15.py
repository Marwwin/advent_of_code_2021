import day15
def test_create_priority_queue():
  queue = day15.PriorityQueue()
  assert not queue.is_empty()

def test_create_queue_with_elements():
  queue = day15.PriorityQueue([(1,(0,1)),(2,(1,0))])
  assert queue.is_empty()

def test_get_left_element():
  queue = day15.PriorityQueue([(1,(0,1)),(2,(1,0)),(3,(1,1)),(4,(2,1))])
  assert queue.get_left(1) == (4,(2,1))
  assert queue.get_left(0) == (2,(1,0))

def test_get_right_element():
  queue = day15.PriorityQueue([(1,(0,1)),(2,(1,0)),(3,(1,1)),(4,(2,1)),(5,(2,2))])
  assert queue.get_right(0) == (3,(1,1))
  assert queue.get_right(1) == (5,(2,2))

def test_insert_element():
  queue = day15.PriorityQueue([(1,(0,1)),(2,(1,0)),(3,(1,1))])
  queue.insert((20,(2,2)))
  assert queue.get_left(1) == (20,(2,2))

def test_pop_min_element():
  queue = day15.PriorityQueue([(1,(0,1)),(2,(1,0)),(3,(1,1))])
  item = queue.pop()
  assert item == (1,(0,1))
  
def test_when_popping():
  queue = day15.PriorityQueue([(10,(0,1)),(20,(1,0)),(30,(1,1)),(40,(2,2)),(50,(2,3))])
  assert queue.length() == 5
  queue.pop()
  item = queue.pop()
  assert item == (20,(1,0))
  assert queue.length() == 3

def test_swap():
  queue = day15.PriorityQueue([(1,(0,1)),(2,(1,0)),(3,(1,1))])
  queue.swap(0,1)
  first = queue.pop()
  second = queue.pop()
  assert first == (2,(1,0))
  assert second == (1,(0,1))

def test_heapify():
  queue = day15.PriorityQueue([(10,(0,1)),(20,(1,0)),(30,(1,1))])
  queue.insert((5,(10,10)))
  item = queue.pop()
  assert item == (5,(10,10))

def test_get_parent():
  queue = day15.PriorityQueue([(10,(0,1)),(20,(1,0)),(30,(1,1)),(40,(2,2))])
  assert queue.get_parent(1) ==(10,(0,1))
  assert queue.get_parent(3) == (20,(1,0))

def test_get_parent_idx():
  queue = day15.PriorityQueue([(10,(0,1)),(20,(1,0)),(30,(1,1)),(40,(2,2))])
  assert queue.get_parent_idx(4) == 1

