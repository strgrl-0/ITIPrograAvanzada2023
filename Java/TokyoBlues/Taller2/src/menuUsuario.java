import java.util.Scanner;

public class menuUsuario {

    public static void mostrarIas(ListaIa listaIa){ 
        
    }
   //1
    public static void agregarDebilidadIA(ListaIa listaIa) {
        for (int i = 0; i < listaIa.getCantIa(); i++) {
            Ia ia = listaIa.getLista()[i];
            if (ia.getDebilidad().equals("") || ia.getDebilidad() == null) {
                System.out.println(ia.toString());
            }
        }

        String nombreIa = terminalPedir("Ingrese nombre de ia que desea modificar debilidad"); 
        String debilidadIA = terminalPedir("Ingrese debilidad de la ia que desea agregar"); 
        Ia ia = extraerIA(nombreIa, listaIa); 
        int iaPocision = extraerPocisionDeIA(nombreIa, listaIa); 
        ia.setDebilidad(debilidadIA);
        listaIa.getLista()[iaPocision] = ia;
    }

    //2
    public static void modificarDatosUsuario(ListaUsuarios listaUsuarios) {
        String usuario = terminalPedir("ingrese nombre de usuario que desea modificar");
        String contraseña = terminalPedir("ingrese nueva contraseña");
        Usuario user = extraerUsuario(usuario, listaUsuarios);
        int pocisionUser = extraerPocisionDeUsuario(usuario, listaUsuarios);

        user.setContraseña(contraseña);
        listaUsuarios.getListaUsuarios()[pocisionUser] = user; 
    }



    public static Usuario extraerUsuario(String usuario, ListaUsuarios listaUsuarios) {
        for (int i = 0; i < listaUsuarios.getCantUsuarios(); i++) {
            if (listaUsuarios.getListaUsuarios()[i].getNombre().equals(usuario)) {
                return listaUsuarios.getListaUsuarios()[i]; 
            }
        }
        return null; 
    }



    public static int extraerPocisionDeUsuario(String usuario, ListaUsuarios listaUsuarios) {
        for (int i = 0; i < listaUsuarios.getCantUsuarios(); i++) {
            if (listaUsuarios.getListaUsuarios()[i].getNombre().equals(usuario)) {
                return i; 
            }
        }
        return 0; 
    }
    

    //3
    public static void modificarPrecisionIA(ListaIa listaIa) {
        String nombre = terminalPedir("ingrese nombre de ia que desea modificar");
        String precision = terminalPedir("ingrese nueva precision deseada"); 
        if(Integer.parseInt(precision)>100 || Integer.parseInt(precision)<0){
            System.out.println("Precision no puede ser mayor que 100 o menor que 0");    
        }

        int pocisionIa = extraerPocisionDeIA(nombre, listaIa);
        Ia ia = extraerIA(nombre, listaIa);
        ia.setPrecision(precision);
        listaIa.getLista()[pocisionIa] = ia;
    }


    public static Ia extraerIA(String ia, ListaIa listaIa) {
        for (int i = 0; i < listaIa.getCantIa(); i++) {
            if (listaIa.getLista()[i].getNombre().equals(ia)) {
                return listaIa.getLista()[i];
            } else{
                System.out.println("No existe la IA");
            }
        }
        return null; 
    }





    public static int extraerPocisionDeIA(String ia, ListaIa listaIa) {
        for (int i = 0; i < listaIa.getCantIa(); i++) {
            if (listaIa.getLista()[i].getNombre().equals(ia)) {
                return i; 
            }
        }
        return 0; 
    }

    //4
    public static void verIA(ListaIa listaIa) {
        for (int i = 0; i < listaIa.getCantIa(); i++) {
            System.out.println(listaIa.getLista()[i].toString());
        }
    }

    //5
    public static void verTiposIA(ListaIa listaIa) {
        String tipo = terminalPedir("que tipo de ia desea ver?");
        boolean seguir = false;
        switch(tipo){
            case "IA AUTONOMA MILITAR":
                seguir=true;
                break;
            case "IA SUPERVISORA":
                seguir=true;
                break;
            case "IA TRANSHUMANISTA":
                seguir=true;
                break;
            case "IA SOCIAL":
                seguir=true;
                break;
            case "IA REALIDAD VIRTUAL":
                seguir=true;
                break;
            default:
                System.out.println("Ia no existe, ingrese de nuevo");
                break;
        }   

        if (seguir==true){
            for (int i = 0; i < listaIa.getCantIa(); i++) {
                if (listaIa.getLista()[i].getTipo().equals(tipo)) {
                    System.out.println(listaIa.getLista()[i].toString());
                }
            }
        }
    }

    public static String terminalPedir(String mensaje) {
        Scanner scan = new Scanner(System.in);
        System.out.println(mensaje);
        return scan.nextLine().toUpperCase(); 
    }

}
