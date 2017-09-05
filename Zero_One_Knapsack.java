import java.util.Scanner;

/**
 * Created by TITASH MANDAL on 9/5/2017.
 */
public class Zero_One_Knapsack {

    public int calculate_max_value(int[] weight, int[] value, int total_weight) {

        int[][] store=new int[(value.length)+1][total_weight+1];

        // The rows of the matrix is till the number of values
        // the cols are all the individual lengths

        for(int i=0;i<=value.length;i++){
            for(int j=0;j<=total_weight;j++){
                if(i==0 || j==0){
                    store[i][j]=0;
                }
                else if(weight[i-1]<=j){
                    //Taking the weight we need to know the value , and remaining weight
                    // or the previous calculated value
                    store[i][j]=Math.max(value[i]+store[i-1][j-weight[i-1]],store[i-1][j]);
                    
                }
                else{
                    store[i][j]=store[i-1][j];
                }
            }
        }
        return store[value.length][total_weight];
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        Zero_One_Knapsack object=new Zero_One_Knapsack();
        int total_weight;
        System.out.println("ENTER TOTAL WEIGHT OF THE KNAPSACK: ");
        total_weight=sc.nextInt();

        System.out.println("Enter the number of weights you want to enter: ");
        int number_of_values=sc.nextInt();

        int[] weight=new int[number_of_values];

        //Enter the weights whose values you have
        for(int i=0;i<number_of_values;i++){
            System.out.println("enter weights: ");
            weight[i]=sc.nextInt();
        }
        //Enter values for corresponding weights
        int[] value=new int[weight.length];
        for(int i=0;i<weight.length;i++){
            System.out.println("Enter value for "+ weight[i]+"kg ");
            value[i]=sc.nextInt();
        }

        System.out.println(object.calculate_max_value(weight,value,total_weight));
    }
}
