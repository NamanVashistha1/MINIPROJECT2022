package Sort;
public class Bubble
{
    public static void bubble(int array[], int n) 
    {
        
        int i,j;
        int temp;
        for(i=0;i<n-1;i++)
        {
            for( j=0;j<n-i-1;j++)
            {
                if(array[j]>array[j+1])
                {
                    temp = array[j];
                    array[j]=array[j+1];
                    array[j+1]=temp;
                }
            }
        }
        System.out.println("\nSorted Data (BUBBLE SORT) :");
        for(i=0;i<n;i++)
        {
            System.out.print(array[i]+" ");
        }
       

    }  
   
}
