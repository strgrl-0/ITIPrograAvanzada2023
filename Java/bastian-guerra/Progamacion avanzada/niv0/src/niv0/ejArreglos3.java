package niv0;

import java.util.Scanner; //Importar escaner

public class ejArreglos3 {

	public static void main(String[] args) {
	/* Diseñe un algoritmo que genere un vector, de tal manera
	que en cada posición del vector coloque el subíndice
	respectivo. El tamaño del vector es N y debe ser leído desde
	pantalla*/

	//Escaner
	Scanner sc = new Scanner(System.in);
		
	System.out.println("Ingrese el tamaño del vector: ");
	int n  = sc.nextInt(); 
	
	int[] vector = new int[n];
	
	for(int i = 0; i < n; i++){
		vector[i] = i;
	}
	
	System.out.println("El vector generado es:");
	for(int i = 0; i < n;i++){
		System.out.println("Posicion " + i + ": " + vector[i]);	
	}
	
	//Cerrar escaner
	sc.close();
	}//Main
}//Public class
