from QueueLL import QueueLL

def test_is_empty():
    ql = QueueLL()
    assert ql.is_empty()

def test_enq_empty():
    ql = QueueLL()
    ql.enq(5)
    assert not ql.is_empty()

def test_enq_tail():
    ql = QueueLL()
    ql.enq(5)
    assert ql.get_tail() == 5

def test_enq_front():
    ql = QueueLL()
    ql.enq(5)
    assert ql.get_front() == 5

def test_deq():
    ql = QueueLL()
    ql.enq(5)
    assert ql.deq() == 5

def test_deq_empty():
    ql = QueueLL()
    ql.enq(5)
    ql.deq()
    assert ql.is_empty()

def test_enq_many_empty():
    ql = QueueLL()
    ql.enq(15)
    ql.enq(16)
    ql.enq(17)
    assert not ql.is_empty()

def test_enq_many_tail():
    ql = QueueLL()
    ql.enq(15)
    ql.enq(16)
    ql.enq(17)
    assert ql.get_tail() == 17

def test_enq_many_front():
    ql = QueueLL()
    ql.enq(15)
    ql.enq(16)
    ql.enq(17)
    assert ql.get_front() == 15

def test_enq_many_deq():
    ql = QueueLL()
    ql.enq(15)
    ql.enq(16)
    ql.enq(17)
    assert ql.deq() == 15

def test_deq_empty():
    ql = QueueLL()
    assert ql.deq() is None

def test_clear_empty():
    ql = QueueLL()
    ql.enq(5)
    ql.clear()
    assert ql.is_empty()

def test_enq_deq_many():
    ql = QueueLL()
    le = []
    la = []
    for i in range(20,201,10):
        ql.enq(i)
        le.append(i)
    while not ql.is_empty():
        la.append(ql.deq())
    assert le == la
