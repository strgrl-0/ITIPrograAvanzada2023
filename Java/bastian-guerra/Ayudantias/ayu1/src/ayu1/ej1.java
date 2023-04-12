package ayu1;

//Escaner
import java.util.Scanner;

public class ej1 {

	public static void main(String[] args) {
		/*Escriba un programa que reciba un numero entero N por pantalla y muestre si es primo o no.*/
		
		//Escaner
		Scanner sc = new Scanner(System.in);
		
		//variables
		boolean esPrimo = true;
		
		//Pedir numero
		System.out.println("Ingrese el numero a saber si es primo o no: ");
		int num = sc.nextInt();
		
		//comprobacion
		for(int i = 2;i<=num;i++){ //i vale 2 para saber si es divisible ademas del 1
			if(num % i == 0) {
				esPrimo = false;
				break;
			} //if
		}//for
		
		if(esPrimo){
			System.out.println("El numero ingresado es primo: ");
		}else {
			System.out.println("El numero ingresado no es primo: ");
		}
		
		sc.close(); //Cerrrar escaner
	}//Main
}//Public class
