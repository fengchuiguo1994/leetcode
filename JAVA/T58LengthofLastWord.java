public class T58LengthofLastWord {
    public static int lengthOfLastWord(String s) {
        boolean flag = true;
        int count = 0;
        for(int i=s.length()-1;i>=0;i--){
            if(flag){
                if(s.charAt(i)==' '){
                    continue;
                } else {
                    flag = false;
                    count += 1;
                }
            } else {
                if(s.charAt(i)!=' '){
                    count += 1;
                } else {
                    break;
                }
            }
        }
        return count;
    }

    public static void main(String[] args){
        String s = "Hello World";
        s = " ";
        long start = System.currentTimeMillis();
        System.out.println(lengthOfLastWord(s));
        System.out.println(String.format("lengthOfLastWord use time %.10f s",(float)(System.currentTimeMillis()-start)/1000));
    }
}
