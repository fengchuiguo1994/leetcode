import java.util.Arrays;
import java.util.Random;

public class T26RemoveDuplicatesfromSortedArray {
    public static int removeDuplicates(int[] nums){
        int flag = 0;
        int mark = 0;
        for(int i=0;i<nums.length;i++){
            if(i==0){
                flag = nums[i];
                mark = 1;
            } else {
                if(flag != nums[i]){
                    nums[mark] = nums[i];
                    mark += 1;
                    flag = nums[i];
                }
            }
        }
        return mark;
    }

    public static void main(String[] args){
        Random r = new Random();
        int tmpr = r.nextInt(10);
        int[] aa = new int[tmpr];
        for(int i=0;i<tmpr;i++){
            aa[i] = r.nextInt(10);
        }
        Arrays.sort(aa);
        System.out.println(Arrays.toString(aa));

        long start = System.currentTimeMillis();
        System.out.println(removeDuplicates(aa));
        System.out.println(String.format("removeDuplicates use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
