package Sort;

public class Selection{
public static void sel(int arr[],int n){

// SELECTION SORT LOGIC :-
for(int i=0;i<n;i++)
{
int min=i;
for(int j=i+1;j<n;j++)
{
if(arr[min]>arr[j])
{
min = j;
}
}
int temp = arr[i];
arr[i] = arr[min];
arr[min] = temp;
}

//// Printing sorted array.
System.out.println("Sorted Data (SELECTION SORT):");
for(int i=0;i<n;i++){
System.out.print(arr[i]+" ");
}
}
}






