def bubble_sorting(seq):
    length = len(seq) - 1
    print(length)

    for num in range(length, 0, -1):
        print(f'진행상황 : {num}')
        for i in range(num):
            print(i)
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
    return seq

def test_bubble_sort():
    seq = [4, 5, 2, 1, 6, 2 , 7, 10, 13, 8]
    print(bubble_sorting(seq))
    assert (bubble_sorting(seq)== sorted(seq))

test_bubble_sort()