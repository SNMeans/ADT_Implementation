from QueueArray import QueueArray

def test_is_empty():
    qa = QueueArray()
    assert qa.is_empty()

def test_enq_empty():
    qa = QueueArray()
    qa.enq(5)
    assert not qa.is_empty()

def test_enq_tail():
    qa = QueueArray()
    qa.enq(5)
    assert qa.get_tail() == 5

def test_enq_front():
    qa = QueueArray()
    qa.enq(5)
    assert qa.get_front() == 5

def test_deq():
    qa = QueueArray()
    qa.enq(5)
    assert qa.deq() == 5

def test_deq_empty():
    qa = QueueArray()
    qa.enq(5)
    qa.deq()
    assert qa.is_empty()

def test_enq_many_empty():
    qa = QueueArray()
    qa.enq(15)
    qa.enq(16)
    qa.enq(17)
    assert not qa.is_empty()

def test_enq_many_tail():
    qa = QueueArray()
    qa.enq(15)
    qa.enq(16)
    qa.enq(17)
    assert qa.get_tail() == 17

def test_enq_many_front():
    qa = QueueArray()
    qa.enq(15)
    qa.enq(16)
    qa.enq(17)
    assert qa.get_front() == 15

def test_enq_many_deq():
    qa = QueueArray()
    qa.enq(15)
    qa.enq(16)
    qa.enq(17)
    assert qa.deq() == 15

def test_deq_empty():
    qa = QueueArray()
    assert qa.deq() is None

def test_clear_empty():
    qa = QueueArray()
    qa.enq(5)
    qa.clear()
    assert qa.is_empty()

def test_enq_deq_many():
    qa = QueueArray()
    le = []
    la = []
    for i in range(20,201,10):
        qa.enq(i)
        le.append(i)
    while not qa.is_empty():
        la.append(qa.deq())
    assert le == la
