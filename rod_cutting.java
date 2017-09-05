import java.util.Scanner;

/**
 * Created by TITASH MANDAL on 9/5/2017.
 */
public class rod_cutting {
    protected int Profit(int[] price,int n){
        int[] value=new int[n+1];
        value[0]=0;
        for(int i=1;i<=n;i++){
            int max_price=Integer.MIN_VALUE;
            for(int j=0;j<i;j++){
                // Given total length i
                // For length starting from 0---->i
                // if we take value[j]+price[remaining] where remaining is i-j-1
                max_price=Math.max(max_price,price[j]+value[i-j-1]);
            }
            value[i]=max_price;
        }
        return value[n];
    }

    public static void main(String[] args) {
        rod_cutting rodCutting=new rod_cutting();
        Scanner sc=new Scanner(System.in);
        int size;
        System.out.println("Enter the rod's length: ");
        size=sc.nextInt();
        int[] price=new int[size];
        for(int i=0;i<size;i++){
            int temp=i+1;
            System.out.println("Enter price for rod length "+temp);
            int prices=sc.nextInt();
            price[i]=prices;
        }



        System.out.println("Maximum profit is "+rodCutting.Profit(price,size));
    }
}
