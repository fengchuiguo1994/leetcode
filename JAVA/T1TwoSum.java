import java.util.*;

public class T1TwoSum {
    public static void shuffle(int[] arr){
        int length = arr.length;
        Random r = new Random(System.currentTimeMillis());
        for(int i=length-1;i>=0;i--){
            int randInt = r.nextInt(length);
            int tmp = arr[i];
            arr[randInt] = arr[i];
            arr[i] = arr[randInt];
        }
    }

    public static int[] method1(int[] nums,int target){
        for(int i=0;i<nums.length-1;i++){
            for(int j=i+1;j<nums.length;j++){
                if(nums[i]==nums[j]){
                    continue;
                }
                if(nums[i]+nums[j]==target){
                    int[] result = {i,j};
                    return result;
                }
            }
        }
        int[] result = new int[0];
        return result;
    }

    public static int[] method2(int[] nums,int target){
        Map<Integer,Integer> tmpdict = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(tmpdict.containsKey(target-nums[i])){
                int[] result = {tmpdict.get(target-nums[i]),i};
                return result;
            }
            tmpdict.put(nums[i],i);
        }
        int[] result = new int[0];
        return result;
    }

    public static void main(String[] args){
        int N = 1000000;
        int tmpN = 10*N;
        int[] tmpnums = new int[tmpN];
        for(int i=0;i<tmpN;i++){
            tmpnums[i] = i;
        }
        shuffle(tmpnums);
        int[] nums = new int[N];
        System.arraycopy(tmpnums,0,nums,0,N);
        int target = new Random().nextInt(tmpN) + N/10;

        long start = System.currentTimeMillis();
        System.out.println(Arrays.toString(method1(nums,target)));
        System.out.println(String.format("method1 use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));

        start = System.currentTimeMillis();
        System.out.println(Arrays.toString(method2(nums,target)));
        System.out.println(String.format("method1 use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
