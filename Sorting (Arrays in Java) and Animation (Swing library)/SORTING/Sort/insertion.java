package Sort;
        public class insertion
        {
    public static void ins(int Array[], int Size){
        int i,j;
        for (i = 1; i < Size; i++) {
            int Key = Array[i];
            j = i - 1;
  
            while (j >= 0 &&  Array[j] > Key){
                Array[j + 1] = Array[j];
                j--;
            }
            
             Array[j+1] = Key;
        }
        //// Printing sorted array.
System.out.println("Sorted Data (INSERTION SORT):");
for( i=0;i<Size;i++){
System.out.print(Array[i]+" ");
}
   }
}
