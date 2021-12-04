import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Arrays;
import java.util.stream.Collectors;

public class Main {

    static void pretty_print(List<List<Integer>> l) {
        for (int i = 0; i < 5; i++) {
            for(int j = 0; j < 5; j++) {
                System.out.printf("(%d,%d) ", l.get(i*5+j).get(0), l.get(i*5+j).get(1));
            }
            System.out.println();
        }
        System.out.println();
    }

    static List<Integer> init_drawn(Scanner s) {
        
        return    Arrays.asList(s.nextLine().split(","))
                        .stream()
                        .map(x -> Integer.parseInt(x))
                        .collect(Collectors.toList());
        
    }

    static List<List<List<Integer>>> init_boards(Scanner s) {

        List<List<List<Integer>>> boards = new ArrayList<>();

        while (s.hasNext()) {
            List<List<Integer>> board = new ArrayList<>();
            for(int i = 0; i < 25; i++) {
                board.add(Arrays.asList(new Integer[] {s.nextInt(), 0}));        
            }
            boards.add(board);
        }
        return boards;
    }

    static void star1() throws FileNotFoundException {

        Scanner s = new Scanner(new File("input.in"));

        List<Integer> drawn = init_drawn(s);
        List<List<List<Integer>>> boards = init_boards(s);        

        boolean end;
        int board_index = 0;
        int last_drawn = -1;

bingo:  for (int d : drawn) {
            
            System.out.printf("drawn number %d\n", d);
            
            pretty_print(boards.get(51));

            for (int i = 0; i < boards.size(); i++) {
               
                List<List<Integer>> board = boards.get(i);
                for (List<Integer> el : board) {
                    if (el.get(0) == d)
                        el.set(1, 1);
                }

                // check conditions
                for (int j = 0; j < 5; j++) {
                    end = true;
                    for(int k = 0; k < 5; k++) {
                        if (board.get(j * 5 + k).get(1) == 0) {
                            end = false;
                            break;
                        }
                    }
                    if (end) {
                        board_index = i;
                        last_drawn = d;
                        break bingo;
                    }
                    end = true;
                    for(int k = 0; k < 5; k++) {
                        if(board.get(k * 5 + j).get(1) == 0) {
                            end = false;
                            break;
                        }
                    }
                    if (end) {
                        board_index = i;
                        last_drawn = d;
                        break bingo;
                    }
                }
            }
        }

        int sum = 0;
        for(List<Integer> el : boards.get(board_index)) {
            if(el.get(1) == 0)
                sum += el.get(0);
        }

        System.out.printf("Board %d is the best, last number drawn: %d, result=%d\n", 
                board_index, last_drawn, sum * last_drawn);
    }

    static void star2() throws FileNotFoundException {

        Scanner s = new Scanner(new File("input.in"));
        List<Integer> drawn = init_drawn(s);
        List<List<List<Integer>>> boards = init_boards(s);

        boolean end;
        int last_drawn = -1;

bingo:  for (int d : drawn) {
            
            List<Integer> to_remove = new ArrayList<>();

            for (int i = 0; i < boards.size(); i++) {
               
                List<List<Integer>> board = boards.get(i);
                for (List<Integer> el : board) {
                    if (el.get(0) == d)
                        el.set(1, 1);
                }

                // check conditions
check:          for (int j = 0; j < 5; j++) {
                    end = true;
                    for(int k = 0; k < 5; k++) {
                        if (board.get(j * 5 + k).get(1) == 0) {
                            end = false;
                            break;
                        }
                    }
                    if (end) {
                        to_remove.add(i); 
                        last_drawn = d;
                        break check;
                    }
                    end = true;
                    for(int k = 0; k < 5; k++) {
                        if(board.get(k * 5 + j).get(1) == 0) {
                            end = false;
                            break;
                        }
                    }
                    if (end) {
                        to_remove.add(i);
                        last_drawn = d;
                        break check;
                    }
                }
            }

            Collections.sort(to_remove, (x, y) -> y - x); 

            for (int i : to_remove) {
                if (boards.size() == 1) {
                    break bingo;
                }
                boards.remove(i);
            }
        }

        int sum = 0;
        for(List<Integer> el : boards.get(0)) {
            if(el.get(1) == 0)
                sum += el.get(0);
        }

        System.out.printf("The final score for the last board is %d\n", last_drawn * sum);
    }

    public static void main(String[] args) throws FileNotFoundException {
        star1();
        star2();
    }
}

