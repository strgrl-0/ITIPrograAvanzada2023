import java.util.Scanner;

public class menuUsuario {
   
    public static void agregarDebilidadIA(ListaIa listaIa) {
        for (int i = 0; i < listaIa.getCantIa(); i++) {
            Ia ia = listaIa.getLista()[i];
            if (ia.getDebilidad().equals("") || ia.getDebilidad() == null) {
                System.out.println(ia.toString());
            }
        }

        String nombreIa = terminalPedir("ingrese nombre de ia que desea modificar debilidad"); 
        String debilidadIA = terminalPedir("ingrese debilidad de la ia que desea agregar"); 
        Ia ia = extraerIA(nombreIa, listaIa); 
        int iaPocision = extraerPocisionDeIA(nombreIa, listaIa); 
        ia.setDebilidad(debilidadIA);
        listaIa.getLista()[iaPocision] = ia; 
    }

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
    


    public static void modificarPrecisionIA(ListaIa listaIa) {
        String nombre = terminalPedir("ingrese nombre de ia que desea modificar");
        String precision = terminalPedir("ingrese nueva precision deseada"); 
        int pocisionIa = extraerPocisionDeIA(nombre, listaIa);
        Ia ia = extraerIA(nombre, listaIa);
        ia.setPrecision(precision);
        listaIa.getLista()[pocisionIa] = ia;
    }


    public static Ia extraerIA(String ia, ListaIa listaIa) {
        for (int i = 0; i < listaIa.getCantIa(); i++) {
            if (listaIa.getLista()[i].getNombre().equals(ia)) {
                return listaIa.getLista()[i];
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

    public static void verIA(ListaIa listaIa) {
        for (int i = 0; i < listaIa.getCantIa(); i++) {
            System.out.println(listaIa.getLista().toString());
        }
    }

    public static void verTiposIA(ListaIa listaIa) {
        String tipo = terminalPedir("que tipo de ia desea ver?");
        for (int i = 0; i < listaIa.getCantIa(); i++) {
            if (listaIa.getLista()[i].getTipo().equals(tipo)) {
                System.out.println(listaIa.getLista().toString());
            }
        }
    }


    public static String terminalPedir(String mensaje) {
        Scanner scan = new Scanner(System.in);
        System.out.println(mensaje);
        return scan.nextLine(); 
    }

}
