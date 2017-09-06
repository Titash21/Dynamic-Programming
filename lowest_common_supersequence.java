import java.util.Scanner;

/**
 * Created by TITASH MANDAL on 9/6/2017.
 */
public class lowest_common_supersequence {
    int find_length_of_lcs(String string1, String string2, int length1, int length2){
        int[][] lengths=new int[length1+1][length2+1];

        for(int i=0;i<length1;i++){

            for(int j=0;j<length2;j++){

                if(i==0 || j==0){
                    lengths[i][j]=0;
                }

                else if(string1.charAt(i-1)==string2.charAt(j-1)){
                    lengths[i][j]=lengths[i-1][j-1]+1;
                }

                else{
                    lengths[i][j]=Math.max(lengths[i][j-1],lengths[i-1][j]);
                }
            }
        }
        return lengths[length1][length2];
    }
    public static void main(String[] args) {
        lowest_common_supersequence object=new lowest_common_supersequence();
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter first string: ");
        String string1=sc.nextLine();
        System.out.println("Enter second string: ");
        String string2=sc.nextLine();
        int length1=string1.length();
        int length2=string2.length();
        System.out.println(object.find_length_of_lcs( string1,string2,  length1, length2));

    }
}
