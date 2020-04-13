import java.util.*;

public class T14LongestCommanPrefix {
    public static String LongestCommanPrefix(String[] strs){
        if(strs.length<1) {
            return new String();
        }
        int index = 0; // current loci
        boolean flag = true;
        StringBuilder sts = new StringBuilder(); // comman seq
        while(flag){
            if(index >= strs[0].length()){
                break;
            }
            char tmp = strs[0].charAt(index);
            for(int i=0;i<strs.length;i++){
                if(index >= strs[i].length() || strs[i].charAt(index) != tmp){
                    flag = false;
                    break;
                }
            }
            if(flag){
                index += 1;
                sts.append(tmp);
            }
        }
        return sts.toString();
    }

    public static void main(String[] args){
        String words = "qwertyuiopasdfghjklzxcvbnm";
        char[] wordsarr = words.toCharArray();
        StringBuilder prefix = new StringBuilder();
        Random r = new Random();
        int countN = r.nextInt(10);
        for(int i=0;i<countN;i++){
            prefix.append(wordsarr[r.nextInt(26)]);
        }
        countN = r.nextInt(10);
        String[] suf = new String[countN];
        for(int i=0;i<countN;i++){
            int tmpN = r.nextInt(10);
            StringBuilder tmpstr = new StringBuilder();
            for(int j=0;j<tmpN;j++){
                tmpstr.append(wordsarr[r.nextInt(26)]);
            }
            suf[i] = tmpstr.toString();
        }
        if(r.nextInt(2)==1){
            for(int i=0;i<suf.length;i++){
                suf[i] = prefix.append(suf[i]).toString();
            }
        }

        System.out.println(Arrays.toString(suf));
        long start = System.currentTimeMillis();
        System.out.println(LongestCommanPrefix(suf));
        System.out.println(String.format("LongestCommanPrefix use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
