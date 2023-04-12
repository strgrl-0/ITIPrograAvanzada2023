package ayu1;

import java.util.Scanner;

public class ej2 {

	public static void main(String[] args) {
		/*Tomas quiere participar en el maratón de fin de año que se realizara en su ciudad y
		últimamente le está poniendo mucha dedicación a sus entrenamientos. A lo largo del día
		realiza N recorridos de aproximadamente 5 kilómetros alrededor de su casa y necesita una
		forma de obtener el mejor de sus tiempos, para ello, se necesita realizar un programa donde
		Tomas pueda ingresar por pantalla los tiempos obtenidos (minutos) en cada uno de sus N
		recorridos de entrenamiento y luego muestre cual es su mejor tiempo obtenido.
		N se lee desde pantalla.*/

		//Variables
		int mejorT = 0;
		int mejorN = 0;
		
		//Escaner
		Scanner sc = new Scanner(System.in);
		
		//Pedir numero
		System.out.println("Ingrese el numero de recorridos que se realizo: ");
		int reco = sc.nextInt();
		
		for(int i = 0;i<=reco;i++){
			System.out.println("Ingrese" + (i + 1) + "recorrido: ");
			int t = sc.nextInt();
			if(t > mejorT){
				mejorT = t;
				mejorN = (i+1);
			}//if
		}//for
		
		//Imprimir
		System.out.println("El mejor tiempo fue: ");
		System.out.println("Recorrido" + mejorN + "tiempo" + mejorT);
		
		
		sc.close(); //Cerrrar escaner
	}//Main

}//Public class
