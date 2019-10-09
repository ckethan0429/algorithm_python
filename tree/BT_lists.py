def BinarayTreeList(r):
    return [r,[],[]]

def insertLeft(root, newBranch):
    t = root.pop(1)
    # 자식이 있을 때
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    # 자식이 없을 때
    else :
        root.insert(1, [newBranch, [], []])
    return root

def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1 :
        root.insert(2, [newBranch, [], t])

    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def main():
    r = BinarayTreeList(3)
    #왼쪽 자식 삽입
    insertLeft(r,4)
    #왼쪽 자식 삽입 
    insertLeft(r,5)
    #오른쪽 자식 삽입
    insertRight(r,6)
    #오른쪽 자식 삽입
    insertRight(r,7)

    print(getRootVal(r))
    print(getLeftChild(r))
    print(getRightChild(r))


if __name__ == "__main__":
    main()