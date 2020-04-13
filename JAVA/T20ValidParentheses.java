import java.util.*;

public class T20ValidParentheses {
    public static boolean isValid(String s){
        if(s.length()%2!=0){
            return false;
        }

        List<Character> pa = new ArrayList<>();
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='(' || s.charAt(i)=='[' || s.charAt(i)=='{'){
                pa.add(s.charAt(i));
            } else {
                if(pa.size()==0){
                    return false;
                }
                char tmp = pa.remove(pa.size()-1);
                if(!(tmp=='(' && s.charAt(i)==')' ||
                        tmp=='[' && s.charAt(i)==']' ||
                        tmp=='{' && s.charAt(i)=='}')){
                    return false;
                }
            }
        }
        if(pa.size()==0){
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args){
        String words = "(){}[]";
        StringBuilder str = new StringBuilder();
        Random r = new Random();
        int up = r.nextInt(10);
        for(int i=0;i<up;i++){
            str.append(words.charAt(r.nextInt(6)));
        }
        System.out.println(str.toString());

        long start = System.currentTimeMillis();
        System.out.println(isValid(str.toString()));
        System.out.println(String.format("isValid use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
