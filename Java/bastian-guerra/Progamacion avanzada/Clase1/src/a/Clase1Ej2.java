package a;
import java.util.Scanner;

public class Clase1Ej2 {

	public static void main(String[] args) {
		/*Cálculo del promedio de edad. Se leen las edades, hasta que se lee un “-1”,
		 *  que implica el fin de los datos. */

			Scanner leer = new Scanner(System.in);
			int contPersonas = 0;
			int sumEdad = 0;
			
			System.out.println("Ingrese edad: ");
			int edad = leer.nextInt();
			
			while(edad != -1) {
				sumEdad += edad;
				contPersonas++;
				System.out.println("Ingrese edad: ");
				edad = leer.nextInt();
			}
			
			if (contPersonas > 0) {
				int promEdad = sumEdad /contPersonas;
				System.out.println("Promedio edad: " + promEdad);
			}else {
				System.out.println("No se leyeron edades");
			}
			leer.close();
	}

}
