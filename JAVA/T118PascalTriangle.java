import org.omg.PortableInterceptor.INACTIVE;

import java.util.*;

public class T118PascalTriangle {
    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();
        if(numRows == 0){
            return result;
        } else {
            List<Integer> tmp = new ArrayList<>();
            tmp.add(1);
            result.add(tmp);
            if(numRows == 1){
                return result;
            }
            for(int i=1;i<numRows;i++) {
                tmp = new ArrayList<>();
                for(int j=0;j<i+1;j++){
                    if(j == 0){
                        tmp.add(result.get(i-1).get(j));
                    } else if(j == result.get(i-1).size()){
                        tmp.add(result.get(i-1).get(result.get(i-1).size()-1));
                    } else {
                        tmp.add(result.get(i-1).get(j-1)+result.get(i-1).get(j));
                    }
                }
                result.add(tmp);
            }
            return result;
        }
    }

    public static void main(String[] args){
        int x = 5;
        long start = System.currentTimeMillis();
        System.out.println(generate(x));
        System.out.println(String.format("generate use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
