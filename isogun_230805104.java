import java.util.Scanner;

public class Isogun_230805104 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt for the number of students
        System.out.print("Enter the number of students: ");
        int numberOfStudents = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character

        // Initialize variables to store the lowest score and corresponding student name
        String lowestScoreStudent = "";
        double lowestScore = Double.MAX_VALUE; // Set to maximum value initially

        // Loop to input each student's name and score
        for (int i = 0; i < numberOfStudents; i++) {
            System.out.print("Enter the name of student " + (i + 1) + ": ");
            String name = scanner.nextLine();

            System.out.print("Enter the score of " + name + ": ");
            double score = scanner.nextDouble();
            scanner.nextLine(); // Consume the newline character

            // Check if this score is lower than the current lowest score
            if (score < lowestScore) {
                lowestScore = score;
                lowestScoreStudent = name; // Update the lowest score student name
            }
        }

        // Display the name of the student with the lowest score
        System.out.println("The student with the lowest score is: " + lowestScoreStudent + " with a score of " + lowestScore);

        // Close the scanner
        scanner.close();
    }
}