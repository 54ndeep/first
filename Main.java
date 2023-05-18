import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        String[] Moves = {"r","p","s"};
        Random random =new Random();
        Scanner PlayerInput =new Scanner(System.in);


        while (true) {


            String ComputerMoves = Moves[random.nextInt(Moves.length)];
            System.out.println("Pleas Enter Your Move :-");
            String PlayerMove = PlayerInput.nextLine();

            if (PlayerMove.equals("s") || PlayerMove.equals("r") || PlayerMove.equals("p")) {

                if (ComputerMoves.equals(PlayerMove)) {
                    System.out.println("ComputerMove: "+ ComputerMoves+", PlayerMove: "+PlayerMove);
                    System.out.println("Its a tie!");

                }
                if (ComputerMoves.equals("r") && PlayerMove.equals("p")) {
                    System.out.println("ComputerMove: "+ ComputerMoves+", PlayerMove: "+PlayerMove);
                    System.out.println("You Won! ");
                }
                if (ComputerMoves.equals("p") && PlayerMove.equals("s")) {
                    System.out.println("ComputerMove: "+ ComputerMoves+", PlayerMove: "+PlayerMove);
                    System.out.println("You Won! ");
                }
                if (ComputerMoves.equals("s") && PlayerMove.equals("r")) {
                    System.out.println("ComputerMove: "+ ComputerMoves+", PlayerMove: "+PlayerMove);
                    System.out.println("You Won! ");
                }
                if (ComputerMoves.equals("p") && PlayerMove.equals("r")) {
                    System.out.println("ComputerMove: "+ ComputerMoves+", PlayerMove: "+PlayerMove);
                    System.out.println("You Lost! ");
                }
                if (ComputerMoves.equals("s") && PlayerMove.equals("p")) {
                    System.out.println("ComputerMove: "+ ComputerMoves+", PlayerMove: "+PlayerMove);
                    System.out.println("You Lost! ");
                }
                if (ComputerMoves.equals("r") && PlayerMove.equals("s")) {
                    System.out.println("ComputerMove: "+ ComputerMoves+", PlayerMove: "+PlayerMove);
                    System.out.println("You Lost! ");
                }

                System.out.println("Want to play again: yes/no. ");
                String PlayerD = PlayerInput.nextLine();
                if (PlayerD.equals("yes")){
                    break;
                }
            }
            else {
                System.out.println("Not a valid Move!");

            }



        }



    }
}