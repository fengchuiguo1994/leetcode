public class T28ImplementstrStr {
    public static int strStr(String haystack, String needle){
        if(needle.length()==0){
            return 0;
        }
        int len = needle.length();
        for(int i=0;i<haystack.length()-len+1;i++){
            if(haystack.substring(i,i+len).equals(needle)){
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args){
        String haystack = "hello";
        String needle = "ll";

        long start = System.currentTimeMillis();
        System.out.println(strStr(haystack,needle));
        System.out.println(String.format("strStr use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
