package ayu1;

import java.util.Scanner;

public class ej3 {

	public static void main(String[] args) {
		/*Desarrolle un sistema que permita calcular el promedio de un estudiante en una asignatura.
		Al iniciar debe preguntar por el nombre y Rut del estudiante para luego ingresar el nombre
		de la asignatura a analizar “Cálculo” o “Álgebra”:
		• Cálculo está compuesto por 2 pruebas que equivalen a un 70% de la asignatura y un
		control que equivale 30% de la asignatura.
		• Álgebra está compuesto por 1 prueba que equivale a un 80% de la asignatura y 2
		controles cortos que equivalen a un 20%.
		Debe mostrar por pantalla el promedio obtenido.*/

		//Escaner
		Scanner sc = new Scanner(System.in);
		
		//Pedir datos
		System.out.println("Ingrese nombre del estudiante: ");
		String nombre = sc.nextLine();
		System.out.println("Ingrese asignatura(C calculo / A algebra): ");
		String asig = sc.nextLine();
				
		if(asig == "C" || asig == "c"){
			System.out.println("Ingrese la primera nota: ");
			double n1 = sc.nextDouble(); //Prueba 1
			System.out.println("Ingrese la segunda nota: ");
			double n2 = sc.nextDouble(); //Prueba 2
			System.out.println("Ingrese la nota del taller: ");
			double c1 = sc.nextDouble(); //Taller 1
			
			double nc = ((n1 + n2) / 2);
			double promC = (c1 * 0.3) + (nc * 0.7);
			System.out.println("La nota de catedra es: " + promC + " Estudiante: " + nombre);
		}
		
		if(asig == "A" || asig == "a"){
			System.out.println("Ingrese la nota de la pruebaa: ");
			double n1 = sc.nextDouble(); //Prueba 1
			System.out.println("Ingrese la primera nota del taller: ");
			double c1 = sc.nextDouble(); //Taller 1
			System.out.println("Ingrese la segunda nota del taller: ");
			double c2 = sc.nextDouble(); //Taller 1
			
			double ta = ((c1 + c2) / 2);
			double promA = (n1 * 0.8) + (ta * 0.2);
			System.out.println("La nota de algebra es: " + promA + " Estudiante: " + nombre);
		}
		sc.close(); //Cerrrar escaner
	}//Main

}//Pulic class
