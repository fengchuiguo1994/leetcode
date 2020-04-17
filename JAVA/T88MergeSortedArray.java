import java.util.Arrays;

public class T88MergeSortedArray {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int index = n+m-1;
        while(m>0 && n>0){
            if(nums1[m-1] > nums2[n-1]){
                nums1[index] = nums1[m-1];
                m -= 1;
            } else {
                nums1[index] = nums2[n-1];
                n -= 1;
            }
            index -= 1;
        }
        if(n>0){
            for(int i=0;i<n;i++){
                nums1[i] = nums2[i];
            }
        }
    }

    public static void main(String[] args){
        int[] nums1 = {1,2,3,0,0,0};
        int m = 3;
        int[] nums2 = {2,5,6};
        int n = 3;

        long start = System.currentTimeMillis();
        merge(nums1,m,nums2,n);
        System.out.println(Arrays.toString(nums1));
        System.out.println(String.format("merge use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
