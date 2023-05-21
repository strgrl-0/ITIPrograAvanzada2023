import java.io.*;
import java.util.*;

public class App {
	
	/* Archivos de texto
	 *-----------------
	 * Paises.txt
	 * ----------------
	 * Pais,region1,region2,region N
	 * ----------------
	 * Progamadores.txt
	 * ----------------
	 * ID, Nombre, Apellido, Años experiencia, Lenguaje, Lenguaje 2,…, Lenguaje N, País, Ciudad
	 * ---------------
	 * IA.txt
	 * ---------------
	 * Nombre,Lenguaje,Nivel Amenaza,debilidad,pais,precision,tipo,id creador
	 * -> Nivel amenaza desde 1 a 5, 5 más peligroso
	 * -> Debilidad, conocida o desconocida
	 * -> Precision,viene en porcentaje
	 * Helios, Java, 5, desconocida, Chile, 99%, IA autónoma militar, 1
	 * Nova, C#, 2, Desconectar Su base de datos, Chile, 53%, IA social, 2
	 * ----------------
	 * Debilidades.txt
	 * ----------------
	 * Debilidad,Nivel amenaza
	 * Desconectar Su base de datos,3
	 * Formatear Memoria,2
	 * Destruir Neuronas,5
	 * ----------------
	 * Usuarios.txt
	 * ----------------
	 * Nombre usuario,contraseña,id progamador
	 * Pablo#12345, pablo1234,id programador
	 * -> Nombre usuario, contiene la siguiente forma NOMBRE#12345 
	 * -> #Aleatorio que genera sistema, no se debe repetir
	 * */
	
	/*---LECTURA DE ARCHIVOS*/
	
	//Lectura archivo Usuarios.txt,guarda los usuarios en el contenedor listaUsuarios
	public static void leerUsuarios(ListaUsuarios listaUsuarios) throws IOException {
		File archivo = new File("Usuarios.txt");//Archivo
		Scanner sc = new Scanner(archivo);//Escaner
		while(sc.hasNextLine()) {	//Si existe linea...
			String linea[] = sc.nextLine().toUpperCase().split(",");//Separacion de datos por ","
			String nombreUsuario = linea[0].trim().toUpperCase();
			String contrasenaUsuario = linea[1].trim().toUpperCase();
			int idUsuario = Integer.parseInt(linea[2].trim().toUpperCase());
			Usuario usuario = new Usuario(nombreUsuario,contrasenaUsuario,idUsuario);//Creacion de objeto usuario
			listaUsuarios.ingresarUsuario(usuario);//Guarda usuario en el contenedor
		}
		sc.close();
	}
	
	//Lectura archivo Progamadores.txt, guarda los Progamadores en el contenedor listaProgamadores
	public static void leerProgamadores(ListaProgamadores listaProgamadores) throws IOException{
		File archivo = new File("Progamadores.txt"); //Archivo de texto a leer
		Scanner sc = new Scanner(archivo);//Escaneo del archivo
		while(sc.hasNextLine()){ //Mientras tenga siguiente linea...
			String[] linea = sc.nextLine().split(",");
			int id = Integer.parseInt(linea[0]);
			String nombre = linea[1].trim().toUpperCase();
			String apellido = linea[2].trim().toUpperCase();
			int aniosExperiencia = Integer.parseInt(linea[3].trim().toUpperCase());
			int cantLenguajes = (linea.length -2) - 4; //Los lenguajes estan desde la posicion 4 a total -2
			String[] lenguajes = new String[cantLenguajes];//Inicio de arreglo con el tamaño de los lenguaes
			for(int i=0;i<cantLenguajes;i++){
				lenguajes[i] = linea[3 + i].trim();//INgreso de lenguajes en el arreglo
			}
			String pais = linea[4 + cantLenguajes].trim().toUpperCase();
			String ciudad = linea[5 + cantLenguajes].trim().toUpperCase();
			Progamador progamador = new Progamador(id,nombre,apellido,aniosExperiencia,lenguajes,cantLenguajes,pais,ciudad); //Creacion de objeto progamador
			listaProgamadores.ingresarProgamador(progamador);//Ingreso de progamador en el contenedor listaProgamadores
		}
		//Cierre de escaner
		sc.close();
	}
	
	//Lectura archivo IA.txt, guarda las IAS en el contenedor listaIa
	public static void leerIa(ListaIa listaIa) throws IOException {
		//Lectura de archivo
		File archivo = new File("IA.txt");
		Scanner sc = new Scanner(archivo);
		//Ingreso de datos
		while(sc.hasNextLine()){
			String[] linea = sc.nextLine().split(",");
			String nombre = linea[0].trim().toUpperCase();
			String lenguaje = linea[1].trim().toUpperCase();
			int nivelAmenaza = Integer.parseInt(linea[2].trim());
			String debilidad = linea[3].trim().toUpperCase();
			String pais = linea[4].trim().toUpperCase();
			String precision = linea[5].trim().toUpperCase();
			String tipo = linea[6].trim().toUpperCase();
			int idCreador = Integer.parseInt(linea[7].trim());
			Ia ia = new Ia(nombre,lenguaje,nivelAmenaza,debilidad,pais,precision,tipo,idCreador);//Creacion de objeto ia
			listaIa.ingresarIa(ia);//Ingreso de ia en el contenedor listaIa
		}
		//Cierre de escaner
		sc.close();
	}
	
	//Lectura archivo Debilidades.txt, guarda las debilidades en el contenedor listaDebilidades
	public static void leerDebilidades(ListaDebilidades listaDebilidades) throws IOException {
		//Lectura dr archivo
		Scanner sc = new Scanner(new File("Debilidades.txt"));
		//Ingreso de datos
		while(sc.hasNextLine()){
			String[] linea = sc.nextLine().split(",");
			String nombreDebilidad = linea[0].trim().toUpperCase();
			int nivelAmenaza = Integer.parseInt(linea[1]);
			Debilidad debilidad = new Debilidad(nombreDebilidad,nivelAmenaza);//Creacion de objeto debilidad
			listaDebilidades.ingresarDebilidad(debilidad);//Ingreso de debilidad en el contenedor listaDebilidades
		}
		sc.close();
	}
	
	///Lectura archivo Paises.txt, guarda los Paises en el contenedor listaPaises
	public static void leerPaises(ListaPaises listaPaises) throws IOException{
		//Lectura de archivo
		Scanner sc = new Scanner(new File("Países.txt"));
		//Ingreso de datos
		while(sc.hasNextLine()){
			String linea[] = sc.nextLine().split(",");
			String nombre = linea[0].toUpperCase();
			int cantRegiones = (linea.length-1); //Las regiones se ubican luego desde la posicion 2
			String regiones[] = new String[cantRegiones];//Creacion de arreglo con el tamaño de las regiones
			for(int i=0;i<cantRegiones;i++){
				regiones[i] = linea[1+i].trim();//Ingreso de regiones
			}
			Pais pais = new Pais(nombre,cantRegiones,regiones);//Creacion de objeto pais
			listaPaises.ingresarPais(pais);//Ingreso de pais en el contenedor listaPaises
		}
		//Cierre de escaner
		sc.close();
	}
	
	/*---INICIO DE SESION---*/
	
	/*Funcion que recibiendo como parametros los contendores de cada archivo de texto anteriormente leido.
	 * -Pide el usuario y contraseña, en caso de no existir Crea un nuevo usuario.
	 * -En caso de ingresar los requisitos de usuario y contraseña para acceder al menu admin, ingresa*/
	public static void iniciarSesion(ListaUsuarios listaUsuarios,ListaProgamadores listaProgamadores,ListaIa listaIa,ListaDebilidades listaDebilidades,ListaPaises listaPaises){
		Scanner sc = new Scanner(System.in);//Escaner
		//----INICIO DE SESION-----
		System.out.println("----Bienvenido,Inicio de sesion----");
		System.out.println("Ingrese nombre usuario: ");
		String nombreUsuario = sc.nextLine().toUpperCase().trim();
		System.out.println("Ingrese contraseña: ");
		String contrasenaUsuario = sc.nextLine().toUpperCase().trim();
		if(nombreUsuario.equals("EMPANADASCONCHAPALELE") && contrasenaUsuario.equals("SURICATARABIOSA")){
			//Ingreso a menu administrador
			menuAdmin(listaUsuarios,listaProgamadores,listaIa,listaDebilidades,listaPaises);
		}else {
			//Verificacion de usuario existente en el contenedor
			Usuario encontrar = listaUsuarios.verificarUsuario(nombreUsuario,contrasenaUsuario);
			if(encontrar != null) { //Si no retorna nulo significa que existe
				System.out.println("Bienvenido");
				//Mostar por consola el usuario que ingreso
				System.out.println("Usuario= " + encontrar.getNombre() + " " + "Contraseña= " + encontrar.getContraseña());
				menuUsuario(listaUsuarios);
			}else {
				//Si retorna nulo, significa que no fue encontrado el usuario...
				System.out.println("No encontrado");
				System.out.println("¿Desea registrarse? (S/N)");
				String opcion = sc.nextLine().toUpperCase();
				boolean ejecucion = true; //Para la ejecucion del menu de registro
				
				//----MENU DE REGISTRO----
				while(ejecucion) {
					switch(opcion) {
					case "S":
						System.out.println("Ingrese usuario: ");
						nombreUsuario = sc.nextLine().toUpperCase();
						System.out.println("Ingrese contraseña: ");
						contrasenaUsuario = sc.nextLine().toUpperCase();
						//Creacion de usuario
						Usuario nuevoUsuario = listaUsuarios.crearUsuario(nombreUsuario,contrasenaUsuario);
						//Guardar usuario en contenedor
						listaUsuarios.ingresarUsuario(nuevoUsuario);
						System.out.println(listaUsuarios.toString());
						menuUsuario(listaUsuarios);
						//Salida de menu
						ejecucion = false;
						break;
					case "N":
						System.out.println("Saliendo...");
						//Salida de menu
						ejecucion = false;
						break;
					default:
						//Error de ingreso de datoss
						System.out.println("Ingrese opcion nuevamente: ");
						opcion = sc.nextLine().toUpperCase();
					break;	
					}	
				}
			}
		}
		//NO CERRAR ESCANER PARA FUNCIONAMIENTO CORRECTO DEL MAIN
	}
	
	//Funcion encargada de el inicio de sesion de usuario normal
	public static void menuUsuario(ListaUsuarios listaUsuarios) {
		boolean ejecucion = true; //Ejecucion de menu
		String opcion;
		Scanner sc = new Scanner(System.in);//Escaner
		System.out.println("----Bienvenido al menu Usuario----");
		//ejecucion = true, ejecucion del menu
		while(ejecucion) {
			System.out.println("¿A que menu desea ingresar? \n 1- Agregar debilidad IA \n 2- Modificar datos usuario \n"
					+ "3- Modificar precision de una IA \n 4- Ver IAS \n 5- Ver tipos de IA \n 6- Salir");
			opcion = sc.nextLine().toUpperCase().trim();
			//Menu dependiendo de la opcion
			switch(opcion) {
			case "1":
				//Agregar debilidad IA
				break;
			case "2":
				//Modificar datos usuario
				break;
			case "3":
				//Modificar Precision IA
				break;
			case "4":
				//Ver IAS
				break;
			case "5":
				//Ver tipos IA
				break;
			case "6":
				System.out.println("Saliendo...");
				ejecucion = false; //Si ejecucion es falso, sale del menu.
				break;
			default:
				System.out.println("Ingrese nuevamente");
				break;
			}
		}
		sc.close();
	}
	
	public static void menuAdmin(ListaUsuarios listaUsuarios,ListaProgamadores listaProgamadores,ListaIa listaIa,ListaDebilidades listaDebilidades,ListaPaises listaPaises) {
		Scanner sc = new Scanner(System.in);//Escaner
		boolean ejecucion = true;
		//Admin: user =  empanadasconchapalele; contra = suricatarabiosa
		System.out.println("----Bienvenido a Menu Admin----");
		while(ejecucion) {
			System.out.println("¿A que menu desea ingresar? \n 1- Ver Progamadores \n 2- Ver todas las IA \n 3- Editar datos progamador \n "
					+ "4- Editar datos IA \n 5- Editar datos Usuario \n 6- Crear y ver debilidades \n 7- Crear IA-Progamador-Pais \n "
					+ "8-Dar estdisticas Paises \n 9-Salir");
			String opcion = sc.nextLine().trim();
			switch(opcion) {
			case "1":
				//Ver progamadores
				System.out.println("Progamadores \n" + listaProgamadores.toString());
				listaProgamadores.verProgamadores();
				break;
			case "2":
				//Ver las ias
				System.out.println("Ias \n " + listaIa.toString());
				listaIa.verIa();
				break;
			case "3":
				//Editar datos de progamador
				listaProgamadores.editarProgamador();
				break;
			case "4":
				//Editar datos de IA
				listaIa.editarIa();
				break;
			case "5":
				//Editar datos de Usuario
				listaUsuarios.editarUsuario();
				break;
			case "6":
				//Crear debilidad
				listaDebilidades.CrearDebilidad(listaDebilidades);
				break;
			case "7":
				//Crear IA,Progamador,Pais
				System.out.println("Creacion de IA,Progamador o Pais \n ¿Desea crear? (S/M))");
				String opcionCrear = sc.nextLine().trim().toUpperCase(); //Opcion de crear IA
				if(opcionCrear.equals("S")){
					System.out.println("¿Que desea crear? \n 1-IA \n 2-Progamador \n 3-Pais");
					opcionCrear = sc.nextLine().trim();
					switch(opcionCrear) {
					case "1":
						//Creacion de IA
						listaIa.crearIa(listaIa);
						break;
					case "2":
						//Creacion de Progamador
						listaProgamadores.crearProgamador(listaProgamadores);
						break;
					case "3":
						//Creacion de Pais
						listaPaises.crearPais(listaPaises);
						break;
					default:
						System.out.println("Ingrese nuevamente");
						break;
					}
				}else break;
				break;
			case "8":
				listaIa.porcantajePais(listaPaises,listaProgamadores,listaIa);
				//Dar estadisticas por Pais
				break;
			case "9":
				System.out.println("Saliendo...");
				ejecucion = false; //false, Sale del menu Admin
				break;
			default:
				System.out.println("Error,ingrese nuevamente");
				break;
			}
		}
		//Cierre de escaner
		sc.close();
	}
	
	//Creacion de los contenedores,almacenar los datos de las lecturas de archivos e inicio de sesion.
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in); //Iniciar escaner
		int max = 10000; //Tamaño del contenedor 
		
		/*---Contenedores y lectura de archivos---*/
		
		/*---Lista de usuarios.txt---*/
		ListaUsuarios listaUsuarios = new ListaUsuarios(max);//Determinar el tamaño maximo del contenedor
		leerUsuarios(listaUsuarios);//Guarda en el contenedor los usuarios en Usuarios.txt
		System.out.println(listaUsuarios.toString());//Muestra por consola los usuarios
		
		/*---Lista de Progamadores.txt---*/
		ListaProgamadores listaProgamadores = new ListaProgamadores(max,sc);
		leerProgamadores(listaProgamadores);
		System.out.println(listaProgamadores.toString());
		
		/*---Lista de IA.txt---*/
		ListaIa listaIa = new ListaIa(max,sc);
		leerIa(listaIa);
		System.out.println(listaIa.toString());
		
		/*---Lista de Debilidades.txt---*/
		ListaDebilidades listaDebilidades = new ListaDebilidades(max,sc);
		leerDebilidades(listaDebilidades);
		System.out.println(listaDebilidades.toString());
		
		/*---Lista de Paises.txt*/
		ListaPaises listaPaises = new ListaPaises(max,sc);
		leerPaises(listaPaises);
		System.out.println(listaPaises.toString());
		
		System.out.println("empanadasconchapalele  suricatarabiosa ");
		
		//Verificar si el archivo se encuentra vacio
		if(listaUsuarios.getCantUsuarios() == 0 || listaIa.getCantIa() == 0 || listaDebilidades.getCantDebilidad() == 0){
			System.out.println("Algunos de los archivos se encuentra vacio");
		}else {
			iniciarSesion(listaUsuarios,listaProgamadores,listaIa,listaDebilidades,listaPaises);//Iniio de sesion, con opciond de registro en caso de no encontrar usuario
		}
		//Cierre de escaner
		sc.close();
	}

}
