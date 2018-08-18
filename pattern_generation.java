import java.util.*;

class Testing{
	public static void main(String args[])
	{ 
		for (int i = 1; i<6;i++)
		{

			for (int j =0; j<i-1;j++)
				{ 
				System.out.print(" ");
				}
				int k=i;
				while (k < 6){ 
   					System.out.print(k);
   					k++;
				} 
				System.out.println();
		}
	}
}	