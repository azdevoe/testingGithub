import java.util.Scanner;



public class aro_230805041 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("How many students are in the classroom: ");
        int numberOfStudents = input.nextInt();
        if (numberOfStudents <= 0) {
            System.out.println("There are no students in the classroom");
            return;
        }
        double lowestScore = 101; // since the highest score is 100
        StringBuilder lowestNames = new StringBuilder();
        for (int i = 1; i <= numberOfStudents; i++) {
            System.out.print("Enter the name of student " + i + ": ");
            String name = input.next();
            System.out.print("Enter the score of student " + i + ": ");
            double score = input.nextDouble();
            if (score < lowestScore) {
                lowestScore = score;
                lowestNames = new StringBuilder(name);
            } else if (score == lowestScore) {
                lowestNames.append(", ").append(name);
            }
        }
        System.out.println("The student(s) with the lowest score is/are: " + lowestNames.toString() + " with " + lowestScore);
        input.close();
    }
}

