// Lumotos Partition
#include <stdio.h>

// Swap two elements of the array
void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int arr[], int low, int high)
{

    // Set Pivot
    int pivot = arr[high];

    // Set index of where Pivot should be
    int i = low - 1;
    int j = 0;

    // Run a loop from low to high
    for (j = low; j <= high; j++)
    {
        // If index of j is smaller than pivot, we will swap the values at the indexes of i and j
        if (arr[j] < pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    // i+1 represents Correct Position of Pivot...Therefore we swap it with High (The lsat element is our pivot)
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        // Pi is position of the pivot -- that is in the correct position
        int pi = partition(arr, low, high);

        // Separately sort elements before partition and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Function to print the arrray -> C hai :(
void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main(int argc, char const *argv[])
{
    int arr[10];
    printf("Enter 10 numbers in the array:\n");
    for (int i = 0; i < 10; i++)
    {
        scanf("%d", &arr[i]);
    }

    printf("\nUnsorted Array:\n");
    printArray(arr, 10);
    quickSort(arr, 0, 9);
    printf("\nSorted Array\n");
    printArray(arr, 10);

    return 0;
}
