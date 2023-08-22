package Sort;
public class Quick {

    static int partition(int arr[], int low, int high) {
        int pivot = arr[high];
        int i = (low-1);
        
        for (int j=low; j<high; ++j)
        {
            if (arr[j] <= pivot)
            {
                int temp = arr[++i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
 
        int temp = arr[++i];
        arr[i] = arr[high];
        arr[high] = temp;
 
        return i;
    }

     static void sort(int arr[], int low, int high) {
        if (low >= high) return;
        
        int pi = partition(arr, low, high);
        sort(arr, low, pi - 1);
        sort(arr, pi + 1, high);
    }



    public static void quick(int[] arr,int n) {
       
        
        partition(arr, 0, n-1);
      
        System.out.println("\nSorted array: (QUICK SORT)");
        for (int i = 0; i < n; ++i) System.out.print(" " + arr[i]);
    }
}