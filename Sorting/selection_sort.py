
def selection_sorting(seq):
    length = len(seq)
    print(length)
    for i in range(length - 1):
        print(i)
        min_j = i
        for j in range(i+1, length):
            if seq[min_j] > seq[j]:
                min_j = j
        seq[i], seq[min_j] = seq[min_j], seq[i]
        
    return seq


def test_selction_sorting():
    seq = [1, 10, 5, 8, 7, 6, 4,3,2,9]

    assert(selection_sorting(seq)==sorted(seq))
    print('테스트 통과')

if __name__ == "__main__":
    test_selction_sorting()