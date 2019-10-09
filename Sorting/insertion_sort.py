def insertion_sort(seq):
    print(seq)
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
        print(seq)

    return seq


def test_insertion_sort():
    seq = [11,3, 28,43, 9, 4]
    assert(insertion_sort(seq) == sorted(seq))
    print('ㅌㅔ스트통과')

test_insertion_sort()