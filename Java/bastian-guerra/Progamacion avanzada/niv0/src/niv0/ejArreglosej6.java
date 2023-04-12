package niv0;

import java.util.Scanner; //Importar escaner

public class ejArreglosej6 {

	public static void main(String[] args) {
		/*. Leer a, b, c, d, e (reales) desde pantalla y cargarlos en las
		primeras 5 posiciones de un vector.
		Calcular ((a + b) * c) / (d – e) y almacenar el resultado en
		la posición 6 del vector. Considere que (d – e) puede ser 0.*/

		//Variables
		double resultado = 0;
		
		//Escaner
		Scanner sc = new Scanner(System.in);
		
		//Creacion del vector
		double[] vector = new double[6];
		
		//Pedir datos
		System.out.println("Ingrese a: ");
		vector[0] = sc.nextDouble();
		System.out.println("Ingrese b: ");
		vector[1] = sc.nextDouble();
		System.out.println("Ingrese c: ");
		vector[2] = sc.nextDouble();
		System.out.println("Ingrese d: ");
		vector[3] = sc.nextDouble();
		
		//Condicion
		if(vector[3] == vector[4]) {
			System.out.println("El resultado es 0 ");
		} else {
			resultado = ((vector[0] + vector[1]) * vector[2]) / (vector[3] - vector[4]);
			vector[5] = resultado;
			System.out.println("El resultado de la resta es: " + resultado);
		}
		
		//Cerrar escaner
		sc.close();
	}//Main

}//Public class
