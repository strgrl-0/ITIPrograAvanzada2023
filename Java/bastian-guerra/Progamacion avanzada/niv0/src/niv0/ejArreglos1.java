package niv0;

import java.util.Scanner;

public class ejArreglos1 {

	public static void main(String[] args) {
		/* Leer 1000 datos numéricos enteros desde pantalla y
		cargarlos en un vector de 12000 posiciones.*/

		//Escaner
		Scanner sc = new Scanner(System.in);
		
		//Creacion de vector
		int[] vector = new int[12000];
		
		//Ingreso de datos
		for(int i = 0;i < 1000;i++){
			System.out.println("Ingrese el dato #" + (i + 1) + ":");
			int dato = sc.nextInt();
			vector[i] = dato;
		}//For ingreso de datos
		
		//Imprimir en pantalla
		System.out.println("Datos ingresados en el vector:");
		for(int i = 0;i < 1000;i++){
			System.out.println(vector[i] + " ");
		}//For imprimir en pantalla
		
		//Cerrar escaner
		sc.close();
	}//Main

}//Public class
