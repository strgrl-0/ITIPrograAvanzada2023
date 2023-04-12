package ayu2;

//Importar escaner
import java.util.Scanner;

public class ej1 {

	public static void main(String[] args) {
		
	//Creacion de escaner
	Scanner sc = new Scanner(System.in);
	
	System.out.println("Ingrese palabra a saber si es palindromo o no: ");
	String palabra = sc.next();

	//Split para cada letra de la palabra ingresada
	String[] letras = palabra.split("");
	
	//Invertir arreglo
	String[] inverso = new String[letras.length];
	for(int i = 0; i<letras.length;i++){
		inverso[i] = letras[letras.length - 1 - i]; 
	}
	
	//Comparar
	boolean palindromo = true;
	for(int i = 0; i < letras.length;i++){
		if(!letras[i].equals(inverso[i])){
			palindromo = false;
			break;
		}
	}
	
	//Imprimir resultado
	if(palindromo){
		System.out.println(palabra + " Es palindromo");
	}else {
		System.out.println( palabra + " No es palindromo");
	}
	
	//Cerrar escaner
	sc.close();
	}//main

}
