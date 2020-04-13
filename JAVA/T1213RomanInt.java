import java.util.*;

public class T1213RomanInt {
    public static String IntToRoman(int num){
        TreeMap<Integer, String> IntRoman = new TreeMap<>();
        IntRoman.put(1,"I");IntRoman.put(5,"V");IntRoman.put(10,"X");IntRoman.put(50,"L");
        IntRoman.put(100,"C");IntRoman.put(500,"D");IntRoman.put(1000,"M");
        IntRoman.put(4,"IV");IntRoman.put(9,"IX"); IntRoman.put(40,"XL");
        IntRoman.put(90,"XC");IntRoman.put(400,"CD");IntRoman.put(900,"CM");
        int[] order = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        StringBuilder s = new StringBuilder();
        while(num > 0){
            for(int x:order){
                if(num >= x){
                    s.append(IntRoman.get(x));
                    num -= x;
                    break;
                }
            }
        }
        return s.toString();
    }

    public static int RomanToInt(String s){
        TreeMap<String,Integer> IntRoman = new TreeMap<>();
        IntRoman.put("I",1);IntRoman.put("V",5);IntRoman.put("X",10);IntRoman.put("L",50);
        IntRoman.put("C",100);IntRoman.put("D",500);IntRoman.put("M",1000);
        IntRoman.put("IV",4);IntRoman.put("IX",9); IntRoman.put("XL",40);
        IntRoman.put("XC",90);IntRoman.put("CD",400);IntRoman.put("CM",900);
        int total = 0;
        int index = 0;
        while(index < s.length()){
            if (index == s.length()-1 || IntRoman.get(s.substring(index,index+1)) >= IntRoman.get(s.substring(index+1,index+2))){
                total += IntRoman.get(s.substring(index,index+1));
            } else {
                total += IntRoman.get(s.substring(index,index+2));
                index += 1;
            }
            index += 1;
        }
        return total;
    }

    public static void main(String[] args){
        int N = new Random().nextInt(10000);
        System.out.println(N);

        long start = System.currentTimeMillis();
        String s = IntToRoman(N);
        System.out.println(s);
        System.out.println(String.format("IntToRoman use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));

        start = System.currentTimeMillis();
        System.out.println(RomanToInt(s));
        System.out.println(String.format("RomanToInt use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
