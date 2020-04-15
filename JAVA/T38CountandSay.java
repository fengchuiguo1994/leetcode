public class T38CountandSay {
    public static String countAndSay(int n) {
        String k = "1";
        if(n==1){
            return k;
        }
        for(int i=1;i<n;i++){
            StringBuilder newstr = new StringBuilder();
            char flag = k.charAt(0);
            int count = 1;
            for(int j=1;j<k.length();j++){
                if(flag != k.charAt(j)){
                    newstr.append(count);
                    newstr.append(flag);
                    count = 0;
                }
                flag = k.charAt(j);
                count += 1;
            }
            newstr.append(count);
            newstr.append(flag);
            k = newstr.toString();
        }
        return k;
    }

    public static void main(String[] args){
        long start = System.currentTimeMillis();
        System.out.println(countAndSay(3));
        System.out.println(String.format("countAndSay use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
