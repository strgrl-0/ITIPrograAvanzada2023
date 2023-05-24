import java.util.Scanner;

public class GatoFitness
{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);

        while (true) {
            System.out.print("Seleccione tipo de gato (Glotón/Normal/Fin): ");
            String tipo = s.nextLine();

            if (tipo.equals("F")) { break; }
            
            System.out.print("Cuánto pesa el gato (en gramos)? ");
            int gramos = Integer.parseInt(s.nextLine());

            Gato gato;

            if (tipo.equals("G")) {
                gato = new GatoGlotón(gramos);
            } else {
                gato = new GatoNormal(gramos);
            }

            System.out.println("Vamos a ver cuánto puede comer el gato:");

            for (int m = 100; m < 1000; m += 100) {
                if (gato.comer(m)) {
                    System.out.println("El gato comió " + m + " gramos");
                } else {
                    System.out.println("El gato NO comió " + m + " gramos. Saliendo!");
                    break;
                }
            }
            System.out.println("Total: " + gato.getTotal());
            System.out.println();
        }
    }
}