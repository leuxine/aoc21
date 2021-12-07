import java.util.*;
import java.util.stream.Collectors;
import java.io.*;

public class Main {

    static void star1() throws FileNotFoundException {
        
        Scanner s = new Scanner(new File("input.in"));

        List<Integer> pos = Arrays.asList(s.next().split(","))
                                  .stream()
                                  .map(x -> Integer.parseInt(x))
                                  .collect(Collectors.toList());

        Collections.sort(pos, (x, y) -> x - y);

        //System.out.println(Arrays.toString(pos.toArray()));

        int max = Collections.max(pos);
        List<Integer> l = new ArrayList<>();
        
        for(int i = 0; i < max + 1; i++)
            l.add(0);

        for(int p : pos) {
            for(int i = 0; i < max + 1; i++)
                l.set(i, l.get(i) + Math.abs(p-i));
        }

        System.out.printf("min cost: %d\n", Collections.min(l));
    }


    static void star2() throws FileNotFoundException {
        
        Scanner s = new Scanner(new File("input.in"));

        List<Integer> pos = Arrays.asList(s.next().split(","))
                                  .stream()
                                  .map(x -> Integer.parseInt(x))
                                  .collect(Collectors.toList());

        Collections.sort(pos, (x, y) -> x - y);

        //System.out.println(Arrays.toString(pos.toArray()));

        int max = Collections.max(pos);
        List<Integer> l = new ArrayList<>();
        
        for(int i = 0; i < max + 1; i++)
            l.add(0);

        for(int p : pos) {
            int count = 0;
            for(int j = p - 1; j >= 0; j--) {
                count += Math.abs(p - j);
                l.set(j, l.get(j) + count);
            }
            count = 0;
            for(int j = p + 1; j < max + 1; j++) {
                count += Math.abs(p - j);
                l.set(j, l.get(j) + count);
            }
        }

        System.out.printf("min cost: %d\n", Collections.min(l));
    }

    public static void main(String[] args) throws FileNotFoundException {
        star1();
        star2();
    }
}
