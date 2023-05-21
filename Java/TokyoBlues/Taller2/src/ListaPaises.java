import java.util.Scanner;

public class ListaPaises {
	private Pais paises[];
	private int cantPaises;
	private int max;
	private Scanner sc;	
	private Pais pais;
	
	//Constructor
	public ListaPaises(int max,Scanner sc){
		this.max = max;
		this.sc = sc;
		this.pais = pais;
		paises = new Pais[max];
		cantPaises = 0;
	}
	
	//Creacion de pais, correspondiente al menu admin
	public void crearPais(ListaPaises listaPaises){
		boolean ejecucion = true;
		Scanner sc = new Scanner(System.in);
		while(ejecucion){
			System.out.println("Creacion de pais");
			System.out.println("Ingrese nombre del pais");
			String nombrePais = sc.nextLine().trim().toUpperCase();
			System.out.println("Ingrese cantidad de regiones");
			int cantRegiones = sc.nextInt();
			String regiones[] = new String[cantRegiones];
			for(int i=0;i<cantRegiones;i++){
				System.out.println("Ingrese region "+i+" :");
				String region = sc.nextLine().trim().toUpperCase();
				regiones[i] = region;
			}
			Pais pais = new Pais(nombrePais,cantRegiones,regiones);
			listaPaises.ingresarPais(pais);
			System.out.println(pais.toString());
		}
	}
	
	//Ingreso de un pais en el contenedor paises
	public boolean ingresarPais(Pais pais){
		if(cantPaises < max){
			paises[cantPaises] = pais;
			cantPaises++;
			return true;
		}else return false;
	}
	
	//Retorna la cantidad de paises
	public int getCantPaises() {
		return cantPaises;
	}
	
	
	public String getPais(int i) {
		return paises[i].getPais();
	}
	
	public String[] regiones(int i) {
		return paises[i].getRegiones();
	}
	
	//To String
	public String toString() {
		String r = "";
		if(cantPaises == 0){
			System.out.println("No existen paises");
		}else {
			for(int i=0;i<cantPaises;i++){
				r += paises[i] + "\n";
			}	
		}
		return r;
	}
	
}
