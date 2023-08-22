import Sort.*;
import java.util.*;


public class Program
{
    public static void main(String[] args) 
    {
        int Size,i,Ch;
            
            Scanner sc = new Scanner(System.in);
            Size = sc.nextInt();
            int Array[] = new int[Size];
            System.out.println("Enter elements of array:");
            for(i=0;i<Size;i++)
            {
                Array[i] = sc.nextInt();
            }
            System.out.println("Inserted array ");
            for(i = 0; i < Size; i++){
                System.out.print(Array[i]+" ");
            }
           
        do
        {    
            System.out.println("\nList of Sorting Methods:\n1.Bubble Sort\n2.Modified Bubble Sort\n3.Insertion Sort\n4.Selection Sort\n5.Bucket Sort\n6.Heap Sort\n7.Quick Sort\n8.Merge Sort\nEnter Your Choice:");
            Ch = sc.nextInt();

            switch(Ch)
            {
                case 1:
                long startTime = System.nanoTime();
                Bubble.bubble(Array,Size);
                long endTime = System.nanoTime();
                System.out.println("\nTime:"+ (endTime - startTime));
                    
                    break;
                case 2:
                long startT1 = System.nanoTime();
                Modified.modify(Array, Size);
                long endT1 = System.nanoTime();
                System.out.println("\nTime:"+ (endT1 - startT1));
                    
                break;
                case 3:
                long startT2 = System.nanoTime();
                Modified.modify(Array, Size);
                long endT2 = System.nanoTime();
                System.out.println("\nTime:"+ (endT2 - startT2));                
                   
                break;
                case 4:
                long startT3= System.nanoTime();
                Modified.modify(Array, Size);
                long endT3= System.nanoTime();
                System.out.println("\nTime:"+ (endT3 - startT3));
                    break;
                case 5:
                    Bucket.buck(Array , Size);
                    break;
                case 6:
                    Heap.sort(Array, Size);
                    break;
                case 7:
                    Quick.quick(Array, Size);
                    break;
                case 8:
                    Merge.m(Array, Size);
                    break;
                case 9:
                    System.out.println("Program Exited");
                    break;
                default:
                    System.out.println("Invalid Choice.");
            }
        }
        while(Ch!=9);
        
            
          
    }
}