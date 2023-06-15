
import java.util.Scanner;

public class ListaDebilidades {
	private Debilidad listaDebilidades[];
	private int cantDebilidad;
	private int max;
	private Scanner sc;
	private Debilidad debilidad;
	
	//Constructor
	public ListaDebilidades(int max,Scanner sc){
		this.max = max;
		this.sc = sc;
		this.debilidad = debilidad;
		listaDebilidades = new Debilidad[max];
		cantDebilidad = 0;
	}
	
	public int getCantDebilidad() {
		return cantDebilidad;
	}

	//Ingreso de debilidad en el contenedor listaDebilidades
	public boolean ingresarDebilidad(Debilidad debilidad) {
		if(cantDebilidad < max){
			listaDebilidades[cantDebilidad] = debilidad;
			cantDebilidad++;
			return true;
		}else return false;
	}
	
	//Creacion de una debilidad correspondiente al menu Admin
	public void CrearDebilidad(ListaDebilidades listaDebilidad){
		boolean ejecucion = true;
		Scanner sc = new Scanner(System.in);
		while(ejecucion) {
			System.out.println("---Menu Debilidades---");
			System.out.println("A continuacion se muestran todas las debilidades");
			System.out.println(toString());
			System.out.println("¿Desea crear nueva debilidad (S/N)?");
			String opcion = sc.nextLine().trim().toUpperCase();
			if(opcion.equals("S")){
				//Pedir datos
				System.out.println("Creacion de nueva debilidad \n ingrese debilidad");
				String nombreDebilidad = sc.nextLine().trim().toUpperCase();
				System.out.println("Ingrese Nivel amenaza");
				int nivelAmenaza = sc.nextInt();
				//Verificar si el nivel de amenaza es el correcto a los parametros
				if(nivelAmenaza >= 1 && nivelAmenaza <= 5){
					Debilidad debilidad = new Debilidad(nombreDebilidad,nivelAmenaza); //Creacion de objeto debilidad
					listaDebilidad.ingresarDebilidad(debilidad);//Ingreso de debilidad en el contenedor
					System.out.println("Se creo nueva debilidad \n" + toString());
				}else {
				System.out.println("Nivel de amenaza fuera de los parametros");	
				}
			}else {
				ejecucion = false;
			}
			
		}
	}

	public String[] leerDebilidades(){
		String[] debExistentesStr = new String[max];
		for(int i=0; i<cantDebilidad; i++){
			if(listaDebilidades[i].toString()!=debExistentesStr[i]){
				debExistentesStr[i]=listaDebilidades[i].toString();
			}
		}
		
	}	

	//To String
	public String toString() {
		String r = "";
		if(cantDebilidad == 0) {
			System.out.println("No existen datos en debilidades");
		}else {
			for(int i=0;i<cantDebilidad;i++){
				r += listaDebilidades[i].toString() + "\n";
			}
		}
		return r;
	}
}
