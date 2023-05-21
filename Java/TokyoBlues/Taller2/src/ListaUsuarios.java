import java.util.Random;
import java.util.Scanner;

public class ListaUsuarios {
	private Usuario listaUsuarios[];//Contenedor
	private int cantUsuarios;//Cantidad de usuarios
	private int max; //Maximo tamaño del contenedor
	private Scanner sc;
	
	//Constructor
	public ListaUsuarios(int max) {
		listaUsuarios = new Usuario[max];
		cantUsuarios = 0;
		this.max = max;
		this.sc = sc;
	}
	
	
	public int getCantUsuarios() {
		return cantUsuarios;
	}
	
	public Usuario[] getListaUsuarios() {
		return listaUsuarios;
	}

	public void setListaUsuarios(Usuario[] listaUsuarios) {
		this.listaUsuarios = listaUsuarios;
	}

	public int getMax() {
		return max;
	}

	public void setMax(int max) {
		this.max = max;
	}

	public void setCantUsuarios(int cantUsuarios) {
		this.cantUsuarios = cantUsuarios;
	}

	//Ingreso de los usuarios en el contenedor
	public boolean ingresarUsuario(Usuario usuario) {
		if(cantUsuarios < max){
			listaUsuarios[cantUsuarios] = usuario;
			cantUsuarios++;
			return true;
		}else return false;
	}
	
	//----CREACION DE NUEVO USUARIO EN INICIO DE SESION-----
	//Verifica si el usuario y contraseña existen en el contenedor de usuarios
	public Usuario verificarUsuario(String nombreUsuario,String contrasenaUsuario) {
		int i;
		for(i=0;i<cantUsuarios;i++) {
			if(listaUsuarios[i].getNombre().equals(nombreUsuario) && listaUsuarios[i].getContraseña().equals(contrasenaUsuario)){
				break;
			}
		}
		if(i == cantUsuarios){
			return null;
		}else {
			return listaUsuarios[i];
		}
	}
	
	//Generar nuevo usuario con formato NOMBRE#12345
	public String generarNuevoUsuario(String nombreUsuario) {
		Random r = new Random();
		int numeroAleatorio = r.nextInt(90000) + 10000; //Genera numero de 5 digitos
		return nombreUsuario + "#" + numeroAleatorio;
	}
	
	//Generar un id aleatorio para la creacion de nuevo usuario
	public int generarNuevaId(){
		Random r = new Random();
		int i;
		int nuevaIdProgamador = r.nextInt(10000) + 1; //Numero entre 1 a 10000
		for(i=0;i<cantUsuarios;i++){
			if(nuevaIdProgamador == listaUsuarios[i].getId()){
				nuevaIdProgamador = r.nextInt(10000) + 1; //Numero entre 1 a 10000
				break;
			}
		}
		return nuevaIdProgamador;
	}
	
	//Crea un nuevo usuario con generarNuevoUsuario e generarNuevaId
	public Usuario crearUsuario(String nombreUsuario,String contrasenaUsuario) {
		String nombreUsuarioNuevo = generarNuevoUsuario(nombreUsuario);
		int idUsuario = generarNuevaId();
		Usuario usuario = new Usuario(nombreUsuarioNuevo,contrasenaUsuario,idUsuario);
		return usuario;
	}
	
	//Buscar si el id existe en el contenedor de los progamadores
	public boolean buscarId(int id) {
		int i;
		for( i=0;i<cantUsuarios;i++){
			if(listaUsuarios[i].getId() == id){
				break;
			}
		}
		if(i == cantUsuarios) {
			return false;
		}else return true;
	}
	
	//Editar datos de usuario,correspondiente al menu Admin
	public void editarUsuario() {
		int i;
		int id;
		boolean existe;
		boolean ejecucion = true;
		Scanner sc = new Scanner(System.in);
		System.out.println("Ingrese id a cambiar: ");
		System.out.println(listaUsuarios.toString());
		id = sc.nextInt();
		existe = buscarId(id);
		if(existe) {
			for( i=0;i<cantUsuarios;i++){
				if(listaUsuarios[i].getId() == id){
					//Encontro al progamador
					while(ejecucion){
						System.out.println("---Menu Editar Datos IA--- \n 1-Modificar Nombre \n 2-Modificar contraseña"
								+ "\n 3-Modificar id \n 4-Salir ");
						String opcion = sc.nextLine().trim();
						switch(opcion) {
						case "1":
							System.out.println("Ingrese nombre a modificar");
							String nombreUsuario = sc.nextLine().toUpperCase();
							listaUsuarios[i].setNombre(nombreUsuario);
							System.out.println("Se realizo cambio de nombre con exito");
							System.out.println(toString());
							break;
						case "2":
							System.out.println("Ingrese contraseña a modificar");
							String contraseñaUsuario = sc.nextLine().toUpperCase();
							listaUsuarios[i].setNombre(contraseñaUsuario);
							System.out.println("Se realizo cambio de contraseña con exito");
							System.out.println(toString());
							break;
						case "3":
							System.out.println("Ingrese nuevo id a modificar");
							int nuevoId = sc.nextInt();
							existe = buscarId(nuevoId);
							if(existe == false) {
								//Cambiar ID en listaProgamadores
								listaUsuarios[i].setId(nuevoId);
								System.out.println("Se realizo el cambio de id con exito");
								System.out.println(toString());
								//Cambiar ID en usuarios
							}else {
								System.out.println("Ya existe el id");
							}
							break;
						case "4":
							System.out.println("Saliendo...");
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
	
	//Retornar valores de el contenedor
	public String toString() {
		String r = "";
		if(cantUsuarios ==0){
			System.out.println("No existen usuarios");
		}else {
			for(int i=0;i<cantUsuarios;i++){
				r += listaUsuarios[i].toString() + "\n";
			}
		}
		return r;
	}
	
}
