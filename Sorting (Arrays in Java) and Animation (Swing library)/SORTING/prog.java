import java.util.Random;
import java.util.Scanner;

import Sort.*;
public class prog {
 public static void main(String[] args) {
int choice;

Scanner sc = new Scanner(System.in);
do{ 

    System.out.println("Enter Choice:");
    System.out.println("1.Sorting\n2.Exit");
choice = sc.nextInt(); 
switch(choice){

case 1:
   Random r = new Random();
   System.out.println("Enter Size of Array:");
    int Size = sc.nextInt();
    int Array[] = new int[Size];

    for(int i=0; i<Size; i++)
    {
        Array[i] = r.nextInt(3000);
        System.out.println(Array[i]);
    }

if(Size<=100){
    Bucket.buck(Array , Size);
}
else if(Size>100 && Size<=200){
    Selection.sel(Array, Size);
}
else if(Size> 200 && Size<=500){
    int i,j;
    int temp;
    int flag=0;
    for(i=0;i<Size-1;i++)
    {
        for( j=0;j<Size-i-1;j++)
        {
            if(Array[j]>Array[j+1])
            {
                temp = Array[j];
                Array[j]=Array[j+1];
                Array[j+1]=temp;
                flag++;
            }
        }
    }
        if(flag<=(Size/10)){
            insertion.ins(Array ,Size);
        }else{
            Bubble.bubble(Array , Size);
        }

}else if(Size>500 && Size<=1000){
    Heap.sort(Array, Size);
}else if(Size>1000 && Size<=2000){
    Quick.quick(Array, Size);
}else{
    Merge.merge(Array, Size);
} 

break;

case 2:
System.out.println("Program EXITED");
break;

case 3:
default:
System.out.println("Inavlid Choice");

}
} while(choice!=2);

}
}