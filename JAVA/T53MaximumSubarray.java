public class T53MaximumSubarray {
    public static int maxSubArray(int[] nums) {
        int maxpre = nums[0],maxsum = nums[0];
        for(int i=1;i<nums.length;i++){
            if(nums[i] < maxpre+nums[i]){
                // 比较当前数和上一个最大数列+当前数的大小
                // 上一个最大数列+当前数的大小更大，说明上一个最大数列值得添加这个当前数
                maxpre = maxpre+nums[i];
            } else {
                // 当前数更大，说明不用加之前的数列就是更大的，舍弃之前的结果
                maxpre = nums[i];
            }
            if(maxpre > maxsum){
                // 此时maxpre记录的时当前状态的最大数列，
                // 将他和最大数列值比较。
                maxsum = maxpre;
            }
        }
        return maxsum;
    }

    public static void main(String[] args){
        int[] aa = {-2,1,-3,4,-1,2,1,-5,4};
        long start = System.currentTimeMillis();
        System.out.println(maxSubArray(aa));
        System.out.println(String.format("maxSubArray use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
