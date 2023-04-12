package ayu2;

//Importar escaner e matriz
import java.util.Arrays;
import java.util.Scanner;

public class ej3 {

	public static void main(String[] args) {
		
		/*Escriba un programa que ordene de menor a mayor las filas de una matriz según la suma de
		estas. Es decir, las filas estarán ordenadas de menor a mayor suma. Muestre por pantalla la
		matriz antes y después del cambio. Los datos de la matriz se leen por pantalla.*/
		
		//Creacion escner
		Scanner sc = new Scanner(System.in);

		//Leer dimensiones de la matriz
		System.out.println("Ingrese las filas: ");
		int filas = sc.nextInt();
		System.out.println("Ingrese las columnas: ");
		int columnas = sc.nextInt();	
		
		//Creacion de la matriz
		int[][] matriz = new int[filas][columnas];
		
		//leer datos de la matriz
		for(int i = 0; i < filas;i++ ) {
			for(int j = 0; j < columnas;j++ ) {
				System.out.println("Ingrese dato, fila: "+ (i + 1) +" columna: " + (j + 1));
				matriz[i][j] = sc.nextInt();
			}
		}
		
		//Mostrar matriz original
		for(int i = 0;i < filas;i++) {
			System.out.println(Arrays.toString(matriz[i])); //Convierte la matriz a un string para imprimirlo
		}
		
		//Ordeamiento de las filas segun suma
		for(int i = 0;i<filas;i++) {
			int sumaFilaActual= 0;
			for(int j = 0;j < columnas;j++) {
				sumaFilaActual += matriz[i][j]; //Suma de la fila actual
			}
			for(int k = i+1;k<filas;k++){
				int sumaFilaSiguiente = 0;
				for(int j = 0;j<columnas;j++) {
					sumaFilaSiguiente += matriz[k][j]; //Suma de la fila siguiente
				}
				if(sumaFilaSiguiente < sumaFilaActual) {
					//Intercambio de filas
					int[] temp = matriz[i];
					matriz[i] = matriz[k];
					matriz[k] = temp;
					
					//Actualizar suma
					sumaFilaActual = sumaFilaSiguiente;
				}
			}
		}
		
		//Mostrar matriz ordenada
		System.out.println("La matriz ordenada es:");
		for(int i = 0;i < filas;i++) {
			System.out.println(Arrays.toString(matriz[i])); //Convierte la matriz a un string para imprimirlo
		}
		
		
		
		//Cerrar escaner
		sc.close();
	}//Main

}//Public class ej3
