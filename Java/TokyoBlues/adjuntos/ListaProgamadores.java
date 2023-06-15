import java.util.Scanner;

public class ListaProgamadores {
	private Progamador listaProgamadores[];
	private int max;
	private int cantProgamadores;
	private Scanner sc;
	private Progamador progamador;
	
	//Constructor
	public ListaProgamadores(int max,Scanner sc) {
	listaProgamadores = new Progamador[max];
	cantProgamadores = 0;
	this.max = max;
	this.sc = sc;
	this.progamador = progamador;
	}

	//Busqueda del id en la lista de progamadores
	public boolean buscarId(int id) {
		int i;
		for( i=0;i<cantProgamadores;i++){
			if(listaProgamadores[i].getId() == id){
				break;
			}
		}
		if(i == cantProgamadores) {
			return false;
		}else return true;
	}
	
	//Ingreso de progamador en el contenedor listaProgamadores
	public boolean ingresarProgamador(Progamador progamador){
		if(cantProgamadores < max){
			listaProgamadores[cantProgamadores] = progamador;
			cantProgamadores++;
			return true;
		}else return false;
	}
	
	//Creacion de nuevo progamador, correspondiente al menu Admin
	public void crearProgamador(ListaProgamadores listaProgamadores) {
		boolean existe;
		boolean ejecucion = true;
		Scanner sc = new Scanner(System.in);
		while(ejecucion) {
			System.out.println("Ingrese id creador");
			int id = sc.nextInt();
			existe = buscarId(id);
			if(existe == false){
				System.out.println("Ingrese nombre");
				String nombre = sc.nextLine().trim().toUpperCase();
				System.out.println("Ingrese apellido");
				String apellido = sc.nextLine().trim().toUpperCase();
				System.out.println("Ingrese años de experiencia");
				int aniosExperiencia = sc.nextInt();
				System.out.println("¿Cuantos lenguajes domina?");
				int lenguajesDomina = sc.nextInt();
				String lenguajes[] = new String[lenguajesDomina];
				for(int i=0;i<lenguajesDomina;i++){
					System.out.println("Ingrese lenguaje que domina "+i+" :");
					String lenguaje = sc.nextLine().trim().toUpperCase();
					lenguajes[i] = lenguaje;
				}
				System.out.println("Ingrese pais");
				String pais = sc.nextLine().trim().toUpperCase();
				System.out.println("Ingrese ciudad");
				String ciudad = sc.nextLine().trim().toUpperCase();
				Progamador progamador = new Progamador(id,nombre,apellido,aniosExperiencia,lenguajes,lenguajesDomina,pais,ciudad);
				listaProgamadores.ingresarProgamador(progamador);
				System.out.println(progamador.toString());
				break;
			}else {
				System.out.println("El id existe");
				ejecucion = false;
				break;
			}
		}
	}
		
	//Retorna la cantidad de Progamadores
	public int getCantProgamadores() {
		return cantProgamadores;
	}

	//Filta los progamadores por paises
	public void verProgamadoresPais() {
		for(int i=0;i<cantProgamadores;i++){
			System.out.println("-Nombre= "+ listaProgamadores[i].getNombre() + " -Pais= " + listaProgamadores[i].getPais());
		}
		System.out.println();
	}
	
	//Filtra los progamadores por ciudad
	public void verProgamadoresCiudad() {
		for(int i=0;i<cantProgamadores;i++){
			System.out.println("-Nombre= "+ listaProgamadores[i].getNombre() + " -Ciudad= " + listaProgamadores[i].getCiudad());
		}
		System.out.println();
	}
	

	//Filtra los progamadores por años de experiencia
	public void verProgamadoresAniosExperiencia() {
		for(int i=0;i<cantProgamadores;i++){
			System.out.println("-Nombre= "+ listaProgamadores[i].getNombre() + " -Anios de Experiencia= " +listaProgamadores[i].getAniosExperiencia());
		}
		System.out.println();
	}

	//Filtra los progamadores por Lenguajes
	public void verProgamadoresLenguajes() {
		for(int i=0;i<cantProgamadores;i++){
			System.out.println("-Nombre= "+ listaProgamadores[i].getNombre() + " -Lenguajes= " + listaProgamadores[i].getLenguajes().length);
		}
		System.out.println();
	}
	
	//Filtra los progamadores por ID y ordenados de mayor a menor
	public void verProgamadoresId() {		
		//Ordenamiento burbuja
		for(int i=0;i<cantProgamadores;i++) {
			for(int j=0;j<cantProgamadores-i-1;j++){
				if(listaProgamadores[j].getId() < listaProgamadores[j+1].getId()){
					Progamador temp = listaProgamadores[i];
					listaProgamadores[j] = listaProgamadores[j+1];
					listaProgamadores[j+1] = temp;
				}
			}
		}
		//Mostrar por consola los progamadores ordenados de mayor a menor debido al numero de ia
		for(int i=0;i<cantProgamadores;i++){
			System.out.println("-"+listaProgamadores[i].getId()+ " -" + listaProgamadores[i].getNombre());
		}
		System.out.println();
	}
	
	//Ver los progamadores por filtros,correspondiente al menu Admin
	public void verProgamadores() {
		Scanner sc = new Scanner(System.in);
		boolean ejecucion = true;
		while(ejecucion) {
			System.out.println("---Menu Filtros Progamadores---, seleccione que desea ver \n 1-Pais \n 2-Ciudad \n 3-Anios experiencia \n "
					+ "4-Cantidad lenguajes conocidos \n 5-Por ID(Mayor a menor) \n 6-Salir");
			String opcion = sc.nextLine().trim();
			switch(opcion){
			case "1":
				//Filtrar progamadores por pais
				verProgamadoresPais();
				break;
			case "2":
				//Filtrar progamadores por ciudad
				verProgamadoresCiudad();
				break;
			case "3":
				//Filtrar progamadores por años de experiencia
				verProgamadoresAniosExperiencia();
				break;
			case "4":
				//Filtrar progamadores por lenguajes
				verProgamadoresLenguajes();
				break;
			case "5":
				//Filtrar progamadores por ID de mayor a menor
				verProgamadoresId();
				break;
			case "6":
				ejecucion = false;
				break;
			default:
				System.out.println("Error,Ingrese nuavemente");
				break;
			}
		}
	}
	
	//Editar datos de un progamador,correspondiente al menu Admin
	public void editarProgamador() {
		int i;
		int id;
		boolean existe;
		boolean ejecucion = true;
		Scanner sc = new Scanner(System.in);
		System.out.println("Ingrese id a cambiar: ");
		System.out.println(listaProgamadores.toString());
		id = sc.nextInt();
		existe = buscarId(id);
		if(existe) {
			for( i=0;i<cantProgamadores;i++){
				if(listaProgamadores[i].getId() == id){
					//Encontro al progamador
					while(ejecucion){
						System.out.println("---Menu Editar Datos Progamador--- \n 1-Agregar lenguaje \n 2-Agregar años experiencia"
								+ "\n 3-Modificar pais \n 4-Modificar ciudad \n 5-Modificar id \n 6-Modificar nombre "
								+ "\n 7-Modificar apellido \n 8-Salir");
						String opcion = sc.nextLine().trim();
						switch(opcion) {
						case "1":
							//Agregar lenguaje
							break;
						case "2":
							System.out.println("Ingrese años de experiencia a agregar");
							int aniosExperiencia = sc.nextInt();
							aniosExperiencia += listaProgamadores[i].getAniosExperiencia();
							listaProgamadores[i].setAniosExperiencia(aniosExperiencia);
							System.out.println("Se realizo el agrego de años de experiencia con exito");
							System.out.println(listaProgamadores[i].toString());
							break;
						case "3":
							System.out.println("Ingrese pais a modificar");
							String pais = sc.nextLine().trim().toUpperCase();
							listaProgamadores[i].setPais(pais);
							System.out.println("Se realizo el cambio de pais con exito");
							System.out.println(listaProgamadores[i].toString());
							break;
						case "4":
							System.out.println("Ingrese ciudad a modificar");
							String ciudad = sc.nextLine().trim().toUpperCase();
							listaProgamadores[i].setCiudad(ciudad);
							System.out.println("Se realizo el cambio de ciudad con exito");
							System.out.println(listaProgamadores[i].toString());
							break;
						case "5":
							System.out.println("Ingrese nuevo id a modificar");
							int nuevoId = sc.nextInt();
							existe = buscarId(nuevoId);
							if(existe == false) {
								//Cambiar ID en listaProgamadores
								listaProgamadores[i].setId(nuevoId);
								System.out.println("Se realizo el cambio de id con exito");
								System.out.println(listaProgamadores[i].toString());
								//Cambiar ID en usuarios
							}else {
								System.out.println("Ya existe el id");
							}
							break;
						case "6":
							System.out.println("Ingrese nombre a modificar");
							String nombre = sc.nextLine().trim().toUpperCase();
							listaProgamadores[i].setNombre(nombre);
							System.out.println("Se realizo el cambio de apellido con exito");
							System.out.println(listaProgamadores[i].toString());
							break;
						case "7":
							System.out.println("Ingrese apellido a modificar");
							String apellido = sc.nextLine().trim().toUpperCase();
							listaProgamadores[i].setApellido(apellido);
							System.out.println("Se realizo el cambio de apellido con exito");
							System.out.println(listaProgamadores[i].toString());
							break;
						case "8":
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
	
	public int buscarPais(String pais) {
		int cantPaises = 0;
		for(int i=0;i<cantProgamadores;i++){
			if(listaProgamadores[i].getPais().equals(pais)){
				cantPaises++;
			}
		}
		return cantPaises;
	}
	
	public String getRegion(int i) {
		return listaProgamadores[i].getCiudad();
	}
	
	//To String
	public String toString() {
		String r = "";
		if(cantProgamadores == 0){
			System.out.println("No existen progamadores");
		}else {
			for(int i=0;i<cantProgamadores;i++){
				r += listaProgamadores[i].toString() + "\n";
			}
		}
		return r;
	}
	
}
