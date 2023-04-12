package ayu2;

//Importar escaner
import java.util.Scanner;

public class ej2 {

	public static void main(String[] args) {

		/*Un estudiante de Nutrición y Dietética necesita saber el IMC promedio de un grupo de
		personas. Para ello se le ha pedido a usted que escriba un programa que reciba las distintas
		alturas (cm) y masas (kg) de los encuestados (fin de datos = -1). Al finalizar el ingreso de datos,
		el programa debe mostrar la siguiente información:
		• IMC promedio
		• IMC más alto
		• IMC más bajo
		• Porcentaje de personas con IMC sobre el IMC promedio
		• Porcentaje de personas con IMC bajo el IMC promedio
		 	*/
		
		//Creacion de escaner
		Scanner sc = new Scanner(System.in);
		
		//Variables
		double altura = 0,masa = 0,sumImc = 0,imc = 0,imcProm = 0,imcMax = 0,imcMin = 100000000;
		int cont = 0,porMayor = 0, porMenor = 0;
		
		System.out.println("Ingresa los datos de las personas encuestadas(fin de datos = -1): ");
		while(altura != -1 || masa != -1 ) {
			System.out.println("Ingrese Altura(cm)");
			altura = sc.nextDouble();
			
			if(altura != -1){
				System.out.println("Ingrese Masa(cm)");
				masa = sc.nextDouble();
				imc = masa / Math.pow(altura / 100, 2);
				sumImc += imc;
				cont++;
				
				//Maximo
				if(imc > imcMax) {
					imcMax = imc;
				}
				//Minimo
				if(imc < imcMin) {
					imcMin = imc;
				}
			}
				
		}//Ciclo while
		
		//Imprimir datos
		if(cont > 1){
			imcProm = sumImc / cont;
			
		    porMayor = calcularPorMayor(imcProm, imcMax, cont);
	        porMenor = calcularPorMenor(imcProm, imcMin, cont);
			
			System.out.println("IMC promedio: " + imcProm);
			System.out.println("IMC más alto: " + imcMax);
			System.out.println("IMC más bajo: " + imcMin);
			System.out.println("Promedio personas mayores promedio: " + porMayor);
			System.out.println("Promedio personas menores promedio: " + porMenor);
		}else {
			System.out.println("No se encontraron datos");
		}
		//Cerrar escaner
		sc.close();
	}//Main
	   public static int calcularPorMayor(double imcProm, double imcMax, int total) {
	        int cont = 0;
	        for (int i = 0; i < total; i++) {
	            double por = ((imcMax - imcProm) / imcProm) * 100;
	            if (por > 0) {
	                cont++;
	            }
	        }
	        return (cont * 100) / total;
	    }
	    
	    public static int calcularPorMenor(double imcProm, double imcMin, int total) {
	        int cont = 0;
	        for (int i = 0; i < total; i++) {
	            double por = ((imcProm - imcMin) / imcProm) * 100;
	            if (por > 0) {
	                cont++;
	            }
	        }
	        return (cont * 100) / total;
	    }
}//Public class ej2






