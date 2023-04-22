package arch;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class aprendiendo {

	public static void main(String[] args) throws FileNotFoundException {
		
		String[] filamento = new String[100];
		int[] precios = new int[100];
		float[] metros = new float[100];
		int n = leerFilamento(filamento,precios);
		leerPeriodo(n,filamento,precios,metros);
		
	}
	public static int leerFilamento(String[] filamentos, int[] precios) throws FileNotFoundException {
		int n = 0;
		
		Scanner scan = new Scanner(new File("config.txt"));
		n = Integer.parseInt(scan.nextLine());
		int cantFilamentos = 0;
		
		while (scan.hasNextLine()) {
			String[] partes = scan.nextLine().split(",");
			String filamen = partes[0];
			int price = Integer.parseInt(partes[1]);
			
			filamentos[cantFilamentos] = filamen;
			precios[cantFilamentos] = price;
			cantFilamentos++;
		}return n;
	}
	public static void leerPeriodo(int n, String[] filamentos, int[] precios, float[] metros) throws FileNotFoundException {
		int conTrue = 0;
		int contFalse = 0;
		int precioTotal = 0;
		float[] periodos = new float[4];
		
		for(int i = 1; i <= n;i++) {
			float contTiempo = 0;
			String nombreArch = "P"+i+".txt";
			Scanner arch = new Scanner(new File(nombreArch));
			while(arch.hasNextLine()) {
				String[] partes = arch.nextLine().split(",");
				String idPedido = partes[0];
				float metro = Float.parseFloat(partes[1]);
				String detalle = partes[2];
				String filamento = partes[3];
				
				if (detalle.equals("Verdadero")) {
					conTrue++;
					contTiempo += 46*metro;
				}
				if (detalle.equals("Falso")) {
					contFalse++;
					contTiempo += 30*metro;
				}
				
				int indice = buscarIndiceFilamento(filamentos,filamento);
				if (indice != -1) {
					metros[indice] += metro;
					precioTotal += precios[indice];
				}
			}
			periodos[i-1] = contTiempo;
		}
		for (int i = 0; i < periodos.length; i++) {
			if (precios[i] == 0) {
				break;
			}
		}
		periodos = cambioMinutosADias(periodos);
		menorMayor(periodos);
		porcentajeVentasDetalles(conTrue,contFalse);
		imprimirListas(filamentos,precios,metros,precioTotal);
	}
	public static int buscarIndiceFilamento(String[] filamentos,String Filamento) {
		for (int i = 0;i < filamentos.length; i++) {
			if(filamentos[i].equals(Filamento)) {
				return i;
			}
		}return -1;
	}
	public static void porcentajeVentasDetalles(int contT,int contF) {
		int total = contT + contF;
		System.out.println("2) Fueron un total de " + total + " ventas realizadas.");
		System.out.println("-> Las ventas realizasas por detalles Verdadero es de un " + (contT*100)/total + "% respecto al resto.");
		System.out.println("-> Las ventas realizasas por detalles Falso es de un " + (contF*100)/total + "% respecto al resto.");
	}
	public static void imprimirListas( String[] filamentos, int[] precios, float[] metros,int precio) {
		System.out.println("3)");
		
		for (int i = 0; i < filamentos.length; i++) {
			if (precios[i] == 0) {
				break;
			}
			System.out.println("El filamento " + filamentos[i] + ":");
			System.out.println("-> Tuvo un total de " + metros[i] + " metros vendidos.");
			System.out.println("-> Con un precio de " + precios[i] + ".");
			System.out.println(" ");
		}
		System.out.println("El gasto total por todo el metro comprado es de: " + precio + "$");
	}
	public static float[] cambioMinutosADias(float[] lista) {
		
		for (int i = 0; i < lista.length; i++) {
			float cont = 0;
			if (lista[i] == 0) {
				break;
			}
			cont = lista[i]/1440;
			lista[i] = cont;
		}return lista; 
	}
	public static void menorMayor(float[] lista) {
		System.out.println("1) Cada periodo con su cantidad de dias: ");
		System.out.println(" ");
		for (int i = 0; i < lista.length; i++) {
			if (lista[i] == 0) {
				break;
			}
			System.out.println("-> El periodo " + (i+1) + " tardo un total de " + lista[i] + " dias.");
			
		}
		
		float totalMenor = 9999;
		int i1 = 0;
		float totalMayor = -9999;
		int i2 = 0;
		
		for (int i = 0; i < lista.length; i++) {
			if (lista[i] == 0) {
				break;
			}
			if (lista[i] < totalMenor) {
				totalMenor = lista[i];
				i1 = i +1;
			}
			if (lista[i] > totalMayor) {
				totalMayor = lista[i];
				i2 = i + 1;
			}
		}
		System.out.println(" ");
		System.out.println("-->La impresión mas rapida fue en el periodo " + (i1) + " con una cantidad de " + totalMenor + " dias.");
		System.out.println("-->La impresión mas lenta fue en el periodo " + (i2) + " con una cantidad de " + totalMayor + " dias.");
		System.out.println(" ");
	}
}
