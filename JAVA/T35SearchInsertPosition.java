import java.util.*;

public class T35SearchInsertPosition {
    public static int searchInsert(int[] nums, int target) {
        int low = 0;
        int high = nums.length-1;
        int med = (low+high)/2;
        while(low <= high){
            if(target > nums[med]){
                low = med + 1;
            } else if(target < nums[med]) {
                high = med - 1;
            } else {
                return med;
            }
            med = (low+high)/2;
        }
        return low;
    }

    public static void main(String[] args){
        int[] aa = {1,3,5,7,9};
        int target = 4;

        long start = System.currentTimeMillis();
        System.out.println(searchInsert(aa,target));
        System.out.println(String.format("searchInsert use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
