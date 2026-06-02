#include "sorting_algs.h"

int* createArray(int length) {
    int* array = malloc(sizeof(int) * length);
    int* head = array;

    while (length) {
        (*array) = rand();
        array++;
        length--;
    }

    return head;
}

float benchmark(void (*func)(int*, int), int* array, int length) {
    task_args args = { func, array, length };

    clock_t start = clock();

    HANDLE thread = CreateThread(NULL, 0, run_task, &args, 0, NULL);

    if (thread == NULL) {
        return -1.0f;
    }

    DWORD result = WaitForSingleObject(thread, 30000);

    if (result == WAIT_TIMEOUT) {
        TerminateThread(thread, 1);
        CloseHandle(thread);
        return -1.0f;
    }

    CloseHandle(thread);
    return (float)(clock() - start) / CLOCKS_PER_SEC;
}

int main() {
    for (int number_of_items = 10; number_of_items < 1e10; number_of_items = number_of_items * 10) {
        printf("Creating array with %d elements...\n", number_of_items);
        int* array = createArray(number_of_items);

        // Quadratic-Time Algorithms
        printf("Bubble sort - %f seconds.\n", benchmark(bubbleSort, array, number_of_items));
        printf("Insetion sort - %f seconds.\n", benchmark(insertionSort, array, number_of_items));
        printf("Selection sort - %f seconds.\n", benchmark(selection_sort, array, number_of_items));

        // Sub-quadratic and O(n log n) Algorithms

        printf("Shell sort - %f seconds.\n", benchmark(shellsort, array, number_of_items));
        printf("Merge sort - %f seconds.\n", benchmark(mergeSortWrapper, array, number_of_items));
        printf("Heap sort - %f seconds.\n", benchmark(heapSort, array, number_of_items));
        printf("Quick sort - %f seconds.\n", benchmark(quickSortWrapper, array, number_of_items));

        // Linear-Time Algorithms

        printf("Count sort - %f seconds.\n", benchmark(countsort, array, number_of_items));
        printf("Radix sort - %f seconds.\n\n", benchmark(radixSort, array, number_of_items));
    }
    return 0;
}