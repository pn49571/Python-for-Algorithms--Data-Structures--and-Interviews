from Algorithm.Search import binarySearch, linearSearch
from Algorithm.randomNumber import GenerteRandomNumList



def test_bin_search(arr, key, expected):
    arr.sort()
    i = linearSearch.LinearSearch(arr, key).run()
    j = binarySearch.BinarySearch(arr, key, 0, len(arr) - 1).run()

    assert i == j

    if expected:
        assert j >= 0
    else:
        assert j == -1

    print("Linear Search Key found at " + str(i),)
    print(", Binary Search Key found at " + str(j))


def main():
    arr = [5, 3, 2, 9, 7]
    test_bin_search(arr, 5, True)
    test_bin_search(arr, 15, False)

    arr = GenerteRandomNumList.Random(100,0,100).generate()
    test_bin_search(arr, arr[0], True)
    test_bin_search(arr, 1005, False)

    test_bin_search([], 100, False)
    test_bin_search([55], 50, False)
    test_bin_search([55], 55, True)

    print("********Complete*******")

if __name__ == '__main__':
    main()