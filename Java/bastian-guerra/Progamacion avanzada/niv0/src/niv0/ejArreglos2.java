package niv0;

import java.util.Scanner;

public class ejArreglos2 {

	public static void main(String[] args) {
		/*Leer 300 números reales desde pantalla y ubíquelos en las
		posiciones pares de un vector de 1000 posiciones.*/

		
		//Escaner	
		Scanner sc = new Scanner(System.in);
		
		double[] vector = new double[1000];
		int pos = 0; //Posicion
		
		for(int i = 0; i < 1000;i++){
			System.out.println("Ingrese numero real: ");
			double num = sc.nextDouble();
			if(pos < 1000){
				vector[pos] = num;
				pos += 2;
			} else {
				System.out.println("El vector esta lleno: ");
				break;
			}
		
		System.out.println("Los numeros ingresados son:");
		for (i = 0; i < 1000; i+= 2) {
			System.out.println("Posicion " + i + ": " + vector[i]);
		}
		//Cerrar escaner
		sc.close();
	}//main
	}
}
	