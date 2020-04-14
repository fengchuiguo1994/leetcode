import java.util.Arrays;
import java.util.Random;

public class T27RemoveElement {
    public static int removeElement(int[] nums, int val) {
        int mark = 0;
        for(int x:nums){
            if(x!=val){
                nums[mark] = x;
                mark += 1;
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
        int val;
        if(aa.length>0){
            val = aa[r.nextInt(aa.length)];
        } else {
            val = r.nextInt(10);
        }
        System.out.println(Arrays.toString(aa));
        System.out.println(val);

        long start = System.currentTimeMillis();
        System.out.println(removeElement(aa,val));
        System.out.println(String.format("removeElement use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
