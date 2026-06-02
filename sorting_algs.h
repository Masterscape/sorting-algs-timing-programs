#include "helpers.h"

// Quadratic-Time Algorithms

void bubbleSort(int array[], int length) {
    bool swapped = false;

    do {
        swapped = false;

        for (int i = 0; i < (length - 1); i++) {
            if (array[i] > array[i+1]) {

                array[i] ^= array[i+1];
                array[i+1] ^= array[i];
                array[i] ^= array[i+1];

                swapped = true;
            }
        }

    } while (swapped);
}

void insertionSort(int array[], int length) {
    for (int i = 0; i < length; i++) {
        int min = i;

        for (int j = i+1; j < length; j++) {
            if (array[j] < array[min]) {
                min = j;
            }
        }

        array[i] ^= array[min];
        array[min] ^= array[i];
        array[i] ^= array[min];
    }
}

void selection_sort(int array[], int length) {
    int min_index;
    for(int i = 0; i < length - 1; i++) {
        min_index = i;
        for(int j = i + 1; j < length; j++) {
            if(array[min_index] > array[j]) {
                min_index = j;
            }
        }
        if(min_index != i)
        {
            int temp = array[i];
            array[i] = array[min_index];
            array[min_index] = temp;
        }
    }
}

// Sub-quadratic and O(n log n) Algorithms

void shellsort(int array[], int length)
{
    for (int i = length / 2; i > 0; i = i / 2)
    {
        for (int j = i; j < length; j++)
        {
            for(int k = j - i; k >= 0; k = k - i)
            {
                if (array[k+i] >= array[k])
                {
                    break;
                }
                else
                {
                    swap(&array[k], &array[k+i]);
                }
            }
        }
    }
}

void mergeSortWrapper(int array[], int length) {
    mergeSort(array, 0, length);
}

void mergeSort(int array[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        mergeSort(array, left, mid);
        mergeSort(array, mid + 1, right);

        merge(array, left, mid, right);
    }
}

void heapSort(int array[], int length)
{
    for (int i = length / 2 - 1; i >= 0; i--)
        heapify(array, length, i);

    for (int i = length - 1; i > 0; i--)
    {
        int temp = array[0];
        array[0] = array[i];
        array[i] = temp;

        heapify(array, i, 0);
    }
}

void quickSortWrapper(int array[], int length) {
    quickSort(array, 0, length);
}

void quickSort(int array[], int low, int high) {
    if (low < high) {
        int pi = partition(array, low, high);

        quickSort(array, low, pi - 1);
        quickSort(array, pi + 1, high);
    }
}

// Linear-Time Algorithms

void countsort(int array[], int length) {
    int maxval = 0;

    for (int i = 0; i < length; i++) {
        if (array[i] > maxval) {
            maxval = array[i];
        }
    }

    int* cntArr = (int*)calloc(maxval + 1, sizeof(int));

    for (int i = 0; i < length; i++) {
        cntArr[array[i]]++;
    }

    for (int i = 1; i <= maxval; i++) {
        cntArr[i] += cntArr[i - 1];
    }

    int* ans = (int*)malloc(length * sizeof(int));
    for (int i = length - 1; i >= 0; i--) {
        ans[cntArr[array[i]] - 1] = array[i];
        cntArr[array[i]]--;
    }

    for (int i = 0; i < length; i++) {
        array[i] = ans[i];
    }

    free(cntArr);
    free(ans);
}

void radixSort(int arr[], int n) {
    int m = getMax(arr, n); 

    for (int exp = 1; m / exp > 0; exp *= 10)
        radixCountSort(arr, n, exp);
}