package Sort;
public class Modified
{
    public static void modify(int array[], int n) 
    {
        
        int i,j;
        int temp;
        int flag=0;
        for(i=0;i<n-1;i++)
        {
            for( j=0;j<n-i-1;j++)
            {
                if(array[j]>array[j+1])
                {
                    temp = array[j];
                    array[j]=array[j+1];
                    array[j+1]=temp;
                    flag++;
                }
            }
          if(flag==0){
            break;
          }
        }
        System.out.println("\nSorted Data (MODIFIED BUBBLE SORT) :");
        for(i=0;i<n;i++)
        {
            System.out.print(array[i]+" ");
        }
        System.out.println("\nFlag:"+flag);
    }    
}
