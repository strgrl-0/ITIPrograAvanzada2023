package niv0;

import java.util.Scanner; //Importar escaner

public class ejArreglos5 {

	public static void main(String[] args) {
		/*Leer desde pantalla un arreglo de reales cuyo tamaño es N,
		donde N viene como primer dato. Calcular e imprimir el
		promedio de los elementos del arreglo que se encuentran
		entre 10 y 25 y que sean mayores que el promedio*/

		//Variables
		double suma = 0; //Suma de datos para el calculo del promedio
		int cont = 0; //Cantidad de datos que cumplen la condicion
		
		//Escaner
		Scanner sc = new Scanner(System.in);
		
		//Pedir n
		System.out.println("Ingrese el tamaño del vector: ");
		int num = sc.nextInt();
		
		//Creacion del vector
		double[] vector = new double[num];
		
		//Ingreso de datos
		for(int i = 0;i < num;i++){
			System.out.println("Ingrese dato" + (i+1) + ": ");
			vector[i] = sc.nextDouble();
			suma += vector[i];
		}
		
		//Promedio
		double prom = suma / num;
		
		//Conidicion
		for(int i = 0;i < num;i++) {
			if(vector[i] > prom && vector[i] >= 10 && vector[i] <= 25){
			prom += vector[i];
			cont++;
			}
		}
		
		//Imprimir datos
		if(cont > 0){
			prom /= cont;
			System.out.println("El promedio de los elementos que se encuentran entre 10 y 25 es:" + prom);
		}else {
			System.out.println("No existen elementos que cumplen con los criterios");
		}
		
		
		//Cerrar escaner
		sc.close();
	}//Main

}//Public class
