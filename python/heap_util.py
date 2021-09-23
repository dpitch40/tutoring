def heap_parent(i):
    return (i - 1) // 2

def left_heap_child(i):
    return 2*i + 1

def right_heap_child(i):
    return 2*i + 2

def visualize_heap(l):
    length = len(l)
    start_row = 0
    end_row = 0
    rows = list()
    while start_row < length:
        rows.append(l[start_row:end_row+1])
        start_row = left_heap_child(start_row)
        end_row = right_heap_child(end_row)

    return '\n'.join(map(str, rows))

def is_heap(l):
    length = len(l)
    for i, v in enumerate(l):
        left_child = left_heap_child(i)
        right_child = right_heap_child(i)
        if left_child < length and l[left_child] > v:
            return False
        if right_child < length and l[right_child] > v:
            return False
    return True