package niv0;

import java.util.Scanner; //Importar escaner

public class ejArreglos4 {

	public static void main(String[] args) {
	/*Leer 100 valores enteros desde pantalla y desplegar la
	cantidad de elementos que son mayores que el promedio.*/

	//Variables
	double prom = 0;
	int mayor = 0;
		
	//Escaner
	Scanner sc = new Scanner(System.in);
	
	//Creacion de vector
	double[] vector = new double[100];
	
	
	for(int i = 0; i < 100;i++){
		System.out.println("Ingrese un numero: ");
		vector[i] = sc.nextInt();
		prom += vector[i];
	}
	
	prom /= 100;
	
	for (int i = 0; i < 100;i++) {
		if(vector[i] > prom) {
			mayor++;
		}
	}
	System.out.println("El promedio de los numeros ingresados es: " + prom);
	System.out.println("La cantidad de numeros mayores que el promedio es: " + mayor);
	
	//Cerrar escaner
	sc.close();
	}//main 

}//public class
