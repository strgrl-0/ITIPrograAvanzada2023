package niv0;

//Importar escaner
import java.util.Scanner;

public class ejArreglos8 {

	public static void main(String[] args) {
		/* Inicializar el vector A, de tamaño N, con 1 en las posiciones
		correspondientes a K, donde K se determina según la serie
		de Fibonacci, cuyos 2 primeros términos son F1 y F2 (F1 <
		F2). Las otras posiciones del vector deben ser inicializadas
		con 0. Desplegar el vector resultante. Los valores de F1, F2
		y N deben ser leídos desde pantalla*/
		
		//Escaner
		Scanner sc = new Scanner(System.in);

		//Pedir datos
		System.out.println("Ingrese el tamaño del vector A:");
		int n = sc.nextInt(); //tamaño vector
		System.out.println("Ingrese F1:");
		int f1 = sc.nextInt(); 
		System.out.println("Ingrese F2:");
		int f2 = sc.nextInt(); 
		
		//Crear vector
		double[] a = new double[n];
		
		
		
		
	}//Main
}
