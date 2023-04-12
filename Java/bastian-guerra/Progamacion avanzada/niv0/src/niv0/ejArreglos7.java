package niv0;

//Importar escaner
import java.util.Scanner;

public class ejArreglos7 {

	public static void main(String[] args) {
		/* Leer desde pantalla los datos de un vector de enteros de
		tamaño N. Se debe calcular el promedio y luego determinar
		e imprimir los datos y la posición de los que sobrepasan en
		5 al promedio. N es el primer dato a leer.*/
		
		//Variables
		double prom = 0;
		
		//Escaner
		Scanner sc = new Scanner(System.in);

		//Pedir tamaño de vector
		System.out.println("Ingrese el tamaño del vector: ");
		int n = sc.nextInt();
		
		//Crear vector
		double[] vector = new double[n];
		
		for(int i = 0;i<n;i++) {
			System.out.println("Ingrese dato " + (i+1)+ " :");
			vector[i] = sc.nextDouble();
			prom = vector[i];
		}
		//Calculo del promedio
		prom/= n;
		
		for(int i = 0;i<n;i++) {
			if(vector[i] > prom + 5){
				System.out.println("El elemento" + (vector[i]) + "En la posicion" + (i + 1) + "sobrepasa el promedio + 5");
			}
		}
		
		//Cerrar escaner
		sc.close();
	}//main

}
