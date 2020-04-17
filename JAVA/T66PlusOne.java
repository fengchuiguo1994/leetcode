import java.lang.reflect.Array;
import java.util.Arrays;

public class T66PlusOne {
    public static int[] plusOne(int[] digits) {
        int digitsindex = digits.length-1;
        int[] add = {1};
        int addindex = add.length-1;
        int maxindex = (digitsindex > addindex)? digitsindex : addindex;
        int[] result = new int[maxindex+1+1]; // 多一位，不需要的时候舍弃。

        int flag = 0;
        int index = 0;

        while(index <= maxindex){
            if(index <= digitsindex && index <= addindex){
                if(digits[digitsindex-index]+add[addindex-index]+flag >= 10){
                    result[maxindex+1-index] = digits[digitsindex-index]+add[addindex-index]+flag-10;
                    flag = 1;
                } else {
                    result[maxindex+1-index] = digits[digitsindex-index]+add[addindex-index]+flag;
                    flag = 0;
                }
            }
            else if(index > digitsindex){
                if(0+add[addindex-index]+flag >= 10){
                    result[maxindex+1-index] = 0+add[addindex-index]+flag-10;
                    flag = 1;
                } else {
                    result[maxindex+1-index] = 0+add[addindex-index]+flag;
                    flag = 0;
                }
            } else {
                if(digits[digitsindex-index]+0+flag >= 10){
                    result[maxindex+1-index] = digits[digitsindex-index]+0+flag-10;
                    flag = 1;
                } else {
                    result[maxindex+1-index] = digits[digitsindex-index]+0+flag;
                    flag = 0;
                }
            }
            index++;
        }
        if(flag == 1){
            result[0] = 1;
            return result;
        } else {
            int[] result2 = new int[maxindex+1];
            System.arraycopy(result,1,result2,0,maxindex+1);
            return result2;
        }
    }

    public static void main(String[] args){
        int[] s = {1,2,3,5};
        long start = System.currentTimeMillis();
        System.out.println(Arrays.toString(plusOne(s)));
        System.out.println(String.format("plusOne use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
