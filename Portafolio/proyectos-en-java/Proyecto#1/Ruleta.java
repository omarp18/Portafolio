import java.io.*;
import java.util.Random;

public class Ruleta{
    private double dinero;
    public Ruleta() {
        dinero = 100.00;
    }

    
    public void Ruletajuego() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        Random random = new Random();

        

        while (true) {
            System.out.println("Ingresa un número del 0-10 en el que quiera apostar");
            System.out.println("Ingresa 'exit' si deseas terminar");
            String resp = reader.readLine();

            if (resp.equalsIgnoreCase("salir")) {
                System.out.println("Gracias por jugar. Su saldo final es de $" + dinero);
                break;
            }

            int numapuesta;
            try {
                numapuesta = Integer.parseInt(resp);
                if (numapuesta < 0 || numapuesta > 10) {
                    System.out.println("Número inválido. Ingrese un número del 0-10.");
                    continue;
                }
            } catch (Exception e) {
                System.out.println("Entrada inválida. Ingresa un número del 0-10 o 'salir'.");
                continue;
            }

            System.out.print("Ingresa la cantidad que deseas apostar: $");
            double canapuesta;
            try {
                canapuesta = Double.parseDouble(reader.readLine());
                if (canapuesta > dinero || canapuesta < 0) {
                    System.out.println("Cantidad inválida. Debes apostar entre $0 y $" + dinero);
                    continue;
                }
            } catch (Exception e) {
                System.out.println("Cantidad inválida. Ingresa una cantidad válida.");
                continue;
            }

            int result = random.nextInt(11);

            System.out.println("La ruleta ha elegido el número " + result);

            if (numapuesta == result) {
                double winnings = canapuesta * 2;
                dinero += winnings;
                System.out.println("¡Ha acertado el número! Ganaste $" + winnings);
            } else if (numapuesta % 2 == result % 2) {
                double winnings = canapuesta;
                dinero += winnings;
                System.out.println("¡Ha acertado par/impar! Ganaste $" + winnings);
            } else {
                dinero -= canapuesta;
                System.out.println("No ha acertado. Perdio $" + canapuesta);
            }

            System.out.println("Su saldo actual es de $" + dinero);
        }
    }
}

