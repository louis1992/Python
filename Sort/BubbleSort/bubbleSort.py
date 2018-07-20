def loadData(path) :
    f = open(path, 'r')
    data = f.readlines()
    f.close()
    return data

def bubbleSort(data) :
    n = len(data)
    for i in range(n) :
        for j in range(0, n-i-1) :
            if data[j] > data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]

def main() :
    data = loadData('./random.txt')
    bubbleSort(data)

    for i in data :
        print (i)

if __name__ == '__main__' :
    main()

