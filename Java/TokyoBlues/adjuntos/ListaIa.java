	import java.util.Scanner;

public class ListaIa {
	private Ia[] listaIa;
	private int max;
	private int cantIa;
	private Scanner sc;
	private Ia ia;
	private ListaPaises paises[];
	
	//Constructor
	public ListaIa(int max,Scanner sc){
		this.max = max;
		this.sc = sc;
		this.ia = ia;
		this.paises = paises;
		this.listaIa = new Ia[max];
		cantIa = 0;
	}

	public  Ia[] getLista() {
		return listaIa;
	}
	
	//Creacion de IA correspondiente al menu Admin 
	public void crearIa(ListaIa listaIa) {
		boolean ejecucion = true;
		Scanner sc = new Scanner(System.in);
		while(ejecucion) {
			//Pedir datos correspondientes
			System.out.println("Ingrese nombre de IA");
			String nombre = sc.nextLine().trim().toUpperCase();
			System.out.println("Ingrese lenguaje");
			String lenguaje = sc.nextLine().trim().toUpperCase();
			System.out.println("Ingrese Nivel amenaza");
			int nivelAmenaza = sc.nextInt();
			sc.nextLine();
			//Verificr si el nivel amenaza esta dentro de los parametros
			if(nivelAmenaza >= 1 && nivelAmenaza <= 5){
				System.out.println("Ingrese Debilidad");
				String debilidad = sc.nextLine().trim().toUpperCase();
				System.out.println("Ingrese Pais");
				String pais = sc.nextLine().trim().toUpperCase();
				System.out.println("Ingrese precision (1 a 100)");
				String precision1 = sc.nextLine().trim();
				int precision2 = Integer.parseInt(precision1);
				if(precision2 <= 100 && precision2 >= 1){
					precision1 = precision2 + "%"; 
				}else {
					System.out.println("Dato precision fuera de los parametros");
					ejecucion = false;
					break;
				}
				System.out.println("Ingrese tipo");
				System.out.println("1- IA autonoma militar \n 2- IA Supervisora \n 3-IA transhumanista \n 4- IA social "
						+ "\n IA realidad virtual");
				String tipo = sc.nextLine().trim();
				switch(tipo){
				case "1":
					tipo = "IA AUTONOMA MILITAR";
					break;
				case "2":
					tipo = "IA SUPERVISORA";
					break;
				case "3":
					tipo = "IA TRANSHUMANISTA";
					break;
				case "4":
					tipo = "IA SOCIAL";
					break;
				case "5":
					tipo = "IA REALIDAD VIRTUAL";
					break;
				default:
					System.out.println("Ingrese nuevamente");
					break;
				}
				System.out.println("Ingrese id creador");
				int id = sc.nextInt();
				Ia ia = new Ia(nombre,lenguaje,nivelAmenaza,debilidad,pais,precision1,tipo,id); //Creacion de objeto ia
				listaIa.ingresarIa(ia);//Ingreso de ia en el contendor listaIa
				System.out.println(ia.toString());
				break;
			}else {
				System.out.println("Nivel de amenaza fuera de los parametros");
				ejecucion = false;
				break;
			}
		}
	}
	
	//Ingreso de un objeto Ia en el contenedor listaIa
	public boolean ingresarIa(Ia ia) {
		if(cantIa < max){
			listaIa[cantIa] = ia;
			cantIa++;
			return true;
		}else return false;
	}
	
	//Devuelve la cantidad de ias
	public int getCantIa() {
		return cantIa;
	}
	
	//Ver el tipo de Ias
	public void verIaTipo() {
		for(int i=0;i<cantIa;i++){
			System.out.println("-Nombre= " + listaIa[i].getNombre() + " -Tipo= " + listaIa[i].getTipo());
		}
	}
	
	//Ver el nombre de la ias por orden alfabetico
	public void verIaNombre() {
		//Ordenamiento burbuja
		for(int i=0;i<cantIa;i++){
			for(int j=0;j<cantIa - i - 1;j++){
				if(listaIa[j].getNombre().compareTo(listaIa[j+1].getNombre()) > 0 ){
					Ia temp = listaIa[j];
					listaIa[j] = listaIa[j+1];
					listaIa[j+1] = temp;
				}
			}
		}
		
		//Mostrar por pantalla
		for(int i=0;i<cantIa;i++){
			System.out.println("-" +listaIa[i].getNombre());
		}
		
	}
	
	//Ver las precisiones de las ias
	public void verIaPrecision() {
		for(int i=0;i<cantIa;i++){
			System.out.println("-Nombre= " + listaIa[i].getNombre() + " -Precisio= " + listaIa[i].getPrecision());
		}
	}
	
	//Ver el pais de las ias
	public void verIaPais() {
		for(int i=0;i<cantIa;i++){
			System.out.println("-Nombre= " + listaIa[i].getNombre() + " -Paises= " + listaIa[i].getPais());
		}
	}
	
	//Ver el nivel de amenaza las ias
	public void verIaNivel() {
		for(int i=0;i<cantIa;i++){
			System.out.println("-Nombre= " + listaIa[i].getNombre() + " -Nivel de amenaza= " + listaIa[i].getNivelAmenaza());
		}
	}
	
	//Menu encargado de ver las ias con los filtros correspondientes (Tipo-Nombre-Precision-Pais)
	public void verIa() {
		Scanner sc = new Scanner(System.in);
		boolean ejecucion = true;
		while(ejecucion) {
			System.out.println("---Menu Filtros Ias---, seleccione que desea ver \n 1-Tipo \n 2-Nombre(Orden alfabetico) \n 3-Precision \n "
					+ "4-Pais \n 5-Nivel peligro \n 6-Salir");
			String opcion = sc.nextLine().trim();
			switch(opcion){
			case "1":
				verIaTipo();
				break;
			case "2":
				verIaNombre();
				break;
			case "3":
				verIaPrecision();
				break;
			case "4":
				verIaPais();
				break;
			case "5":
				verIaNivel();
				break;
			case "6":
				System.out.println("Saliendo...");
				ejecucion = false;
				break;
			default:
				System.out.println("Error,ingrese nuevamente");
				break;
			}
		}
	}
	
	//Buscar id correspondiente en la lista de ias
	public boolean buscarId(int id) {
		int i;
		for( i=0;i<cantIa;i++){
			if(listaIa[i].getIdCreador() == id){
				break;
			}
		}
		if(i == cantIa) {
			return false;
		}else return true;
	}
	
	//Editar datos de las ias
	public void editarIa() {
		int i;
		int id;
		boolean existe;
		boolean ejecucion = true;
		Scanner sc = new Scanner(System.in);
		System.out.println("Ingrese id a cambiar: ");
		System.out.println(toString());
		id = sc.nextInt();
		existe = buscarId(id);//verifica si el id existe
		if(existe) {
			for( i=0;i<cantIa;i++){
				if(listaIa[i].getIdCreador() == id){
					//Encontro al progamador
					while(ejecucion){
						System.out.println("---Menu Editar Datos IA--- \n 1-Modificar Nombre \n 2-Modificar nivel peligrosidad"
								+ "\n 3-Modificar debilidad \n 4-Modificar precision \n 5-Modificar Pais \n 6-Modificar id "
								+ "\n 7-Salir ");
						String opcion = sc.nextLine().trim();
						switch(opcion) {
						case "1":
							System.out.println("Ingrese nombre a modificar");
							String nombreIa = sc.nextLine().toUpperCase();
							listaIa[i].setNombre(nombreIa);
							System.out.println("Se realizo cambio de nombre con exito");
							System.out.println(toString());
							break;
						case "2":
							System.out.println("Ingrese nivel a modificar");
							int nivelIa = sc.nextInt();
							if(nivelIa >= 1 && nivelIa <= 5){
								listaIa[i].setNivelAmenaza(nivelIa);
								System.out.println("Se realizo cambio de nombre con exito");
								System.out.println(toString());
							}else {
								System.out.println("Nivel no permitido");
							}
							break;
						case "3":
							System.out.println("Ingrese debilidad a modificar");
							String debilidadIa = sc.nextLine().toUpperCase();
							listaIa[i].setDebilidad(debilidadIa);
							System.out.println("Se realizo cambio de debilidad con exito");
							System.out.println(toString());
							break;
						case "4":
							System.out.println("Ingrese precision a modificar (1 a 100)");
							String precisionIa = sc.nextLine();
							int precision = Integer.parseInt(precisionIa);
							if(precision <= 100 && precision >= 1){
								listaIa[i].setPrecision(precisionIa + "%");
								System.out.println("Se realizo cambio de precision con exito");
								System.out.println(toString());
							}else {
								System.out.println("Dato ingresado fuera de los parametros");
							}
							break;
						case "5":
							System.out.println("Ingrese pais a modificar");
							String paisIa = sc.nextLine().toUpperCase();
							listaIa[i].setPais(paisIa);
							System.out.println("Se realizo cambio de pais con exito");
							System.out.println(toString());
							break;
						case "6":
							System.out.println("Ingrese nuevo id a modificar");
							int nuevoId = sc.nextInt();
							existe = buscarId(nuevoId);
							if(existe == false) {
								//Cambiar ID en listaProgamadores
								listaIa[i].setIdCreador(nuevoId);
								System.out.println("Se realizo el cambio de id con exito");
								System.out.println(toString());
								//Cambiar ID en usuarios
							}else {
								System.out.println("Ya existe el id");
							}
							break;
						case "7":
							System.out.println("Saliendo");
							ejecucion = false;
							break;		
						default:
							System.out.println("Error, ingrese nuevamente");
							break;
						}
					}
					return;
				}
			}
		}else {
			System.out.println("No se encontro id");
		}
	}
	
	public void porcantajePais(ListaPaises paises,ListaProgamadores listaProgamadores,ListaIa listaIa){
		Scanner sc = new Scanner(System.in);
		boolean ejecucion = true;
		while(ejecucion){
			System.out.println("---Menu Estadisticas Paises--- \n 1-Porcentaje segun paises \n 2-Porcentaje segun Ciudad \n"
					+ " 3-Salir");
			String opcion = sc.nextLine().trim();
			switch(opcion) {
			case "1":
				System.out.println("---Porcentaje segun paises---");
				int cantPaises = paises.getCantPaises();
				int cantIas = listaIa.getCantIa();
				int cantProgamadores = listaProgamadores.getCantProgamadores();
				for(int i=0;i<cantPaises;i++){
					String nombrePais = paises.getPais(i);
					int paisesIa = buscarPais(nombrePais);
					int paisesProgamadores = listaProgamadores.buscarPais(nombrePais);
					/*---PORCENTAJE DEBIDO A LOS PAISES*/
					//Porcentaje en ias
					if(paisesIa ==0){
						System.out.println("Ninguna ia fue creada en: " + nombrePais);
					}else {
						int porIa = (cantPaises / paisesIa) * 100;
						System.out.println("En "+nombrePais+" El % de creacion de ias fue de "+porIa+"%");
					}
					//Porcentaje en progamadores
					if(paisesProgamadores ==0){
						System.out.println("Ningun progamador tiene residencia en : " + nombrePais);
					}else {
						int porProgamadores = (cantPaises / paisesProgamadores) * 100;
						System.out.println("En "+nombrePais+" El % de progamadores fue de "+porProgamadores+"%");
					}
				}
				break;
			case "2":
				//MALOOOOOOOOOOOOOOOOOOOOOOOOOOOO
				System.out.println("---Porcentaje segun ciudades---");
				cantPaises = paises.getCantPaises();
				cantIas = listaIa.getCantIa();
				cantProgamadores = listaProgamadores.getCantProgamadores();
				int totalRegiones = 0; 
				for(int i=0;i<cantPaises;i++){
					/*---PORCENTAJE DEBIDO A LAS CIUDADES*/
					String nombrePais = paises.getPais(i);
					int cantRegion = 0;
					String[] regiones = paises.regiones(i);
					int cantRegiones = regiones.length;
					totalRegiones += cantRegiones;
					for(int j=0;j<cantRegiones;j++){
						if(listaProgamadores.getRegion(i).equals(regiones[j])){
							cantRegion += 1;
						}else {
							System.out.println("Ningun progamador tiene residencia en : " + regiones[j]);
						}
					}
					if(cantRegion == 0) {
						System.out.println("Ningun progamador tiene residencia en : " + nombrePais);
					}
				}
			case "3":
				System.out.println("Saliendo");
				ejecucion = false;
				break;
			default:
				System.out.println("Ingrese opcion nuevamente");
				break;
			}
		}
	}
	
	public int buscarPais(String pais) {
		int cantPaises = 0;
		for(int i=0;i<cantIa;i++){
			if(listaIa[i].getPais().equals(pais)){
				cantPaises++;
			}
		}
		return cantPaises;
	}
	
	public void agregarDebilidadUsr(int agregarDebilidad){
		
	}
	//To string
	public String toString() {
		String r = "";
		if(cantIa == 0) {
			System.out.println("No existen Ias");
		}else {
			for(int i=0;i<cantIa;i++){
			r += listaIa[i].toString() + "\n";	
			}
		}
		return r;
	}
	
}
