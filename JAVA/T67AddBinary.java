import java.util.Arrays;

public class T67AddBinary {
    public static String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();
        int aindex = a.length()-1;
        int bindex = b.length()-1;
        int maxindex = (aindex > bindex)? aindex:bindex;
        int index = 0;
        int flag = 0;
        while(index <= maxindex){
            int tmp;
            if(index<=aindex && index<=bindex){
                tmp = (int)a.charAt(aindex-index)+(int)b.charAt(bindex-index)+flag-48*2;
            } else if (index > aindex){
                tmp = 0+(int)b.charAt(bindex-index)+flag-48;
            } else {
                tmp = (int)a.charAt(aindex-index)+0+flag-48;
            }
            if(tmp>=2){
                result.append(tmp-2);
                flag = 1;
            } else {
                result.append(tmp);
                flag = 0;
            }
            index++;
        }
        if(flag == 1){
            result.append(1);
        }
        result.reverse();
        return result.toString();
    }

    public static void main(String[] args){
        String a = "1010";
        String b = "1011";
        long start = System.currentTimeMillis();
        System.out.println(addBinary(a,b));
        System.out.println(String.format("addBinary use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
