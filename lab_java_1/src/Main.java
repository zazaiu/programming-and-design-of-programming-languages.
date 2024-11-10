import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        double A = 0, B = 0, C = 0, D = 0;

        if (args.length == 4) {
            try {
                A = Double.parseDouble(args[0]);
                B = Double.parseDouble(args[1]);
                C = Double.parseDouble(args[2]);
                D = Double.parseDouble(args[3]);
            } catch (NumberFormatException | ArrayIndexOutOfBoundsException e) {
                System.out.println("Некорректные параметры командной строки. Вводите коэффициенты с клавиатуры.");
            }
        }

        Scanner scanner = new Scanner(System.in);
        if (A == 0 || B == 0 || C == 0 || D == 0) {
            A = getCoefficient(scanner, "Введите коэффициент A: ", A);
            B = getCoefficient(scanner, "Введите коэффициент B: ", B);
            C = getCoefficient(scanner, "Введите коэффициент C: ", C);
            D = getCoefficient(scanner, "Введите коэффициент D: ", D);
        }

        double Discriminant = B * B - 4 * A * C + 16 * A * A * D;
        if (Discriminant == Double.MAX_VALUE) {
            System.out.println("Уравнение не имеет решений.");
        } else if (Discriminant == Double.MIN_VALUE) {
            System.out.println("Уравнение имеет бесконечно много решений.");
        } else if (Double.isNaN(Discriminant)) {
            System.out.println("Диск3риминант не определен.");
        } else {
            double root1 = (-B + Math.sqrt(Discriminant)) / (4 * A);
            double root2 = (-B - Math.sqrt(Discriminant)) / (4 * A);
            System.out.printf("Два различных действительных корня: x1 = %.8f, x2 = %.8f\n", root1, root2);
        }

        try (scanner) {
            // Scan завершен, ресурс автоматически закрывается
        }
    }

    private static double getCoefficient(Scanner scanner, String message, double defaultValue) {
        double coefficient;
        while (true) {
            try {
                System.out.print(message);
                String input = scanner.nextLine();
                if (input.isEmpty()) {
                    return defaultValue; // Если пустая строка, возвращаем значение по умолчанию
                }
                coefficient = Double.parseDouble(input);
                return coefficient;
            } catch (NumberFormatException e) {
                System.out.println("Некорректное значение. Попробуйте снова.");
            }
        }
    }
}