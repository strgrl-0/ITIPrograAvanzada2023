import java.util.Scanner;

import org.w3c.dom.ranges.Range;

public class App {
    public static void main(String[] args) throws Exception {
       Scanner scan = new Scanner(new File("baraja.txt"));
       String[] file1  = scan.nextLine().split(",");

       String[] file2  = scan.nextLine().split(",");
       String[] file3  = scan.nextLine().split(",");
       String[] file4  = scan.nextLine().split(",");

       
    }

    public static void sort(String[] lista){
        if(ParOImpar(lista)==true){

            ascendente(lista);
        } else {
            descendente(lista);
        }
        
    }

    public static boolean ParOImpar(String[] poi){
        //defecto es false, false = impar
        int size = poi.length - 1;
        if(size % 2 == 0){
            return true;
        }
        return false;
    }

    public static int[] traductorTexANum(String[] lista){
        int[] listaTraducida = new int [lista.length];

        for(int i = 1; i<lista.length; i++){
            switch(lista[i]){
                case "J":
                    lista[i]="11";
                case "Q":
                    lista[i]="12";
                case "K":
                    lista[i]="13";
            }

            listaTraducida[i] = Integer.parseInt(lista[i]);

        }
        return listaTraducida;
    }

    public static String[] traductorNumATex(int[] lista){
        String[] listaTraducida = new String [lista.length];

        for(int i = 1; i<lista.length; i++){
            listaTraducida[i] = Integer.toString(i);
            switch(lista[i]){
                case 11:
                    listaTraducida[i] = "J";
                case 12:
                    listaTraducida[i] = "Q";
                case 13:
                    listaTraducida[i] = "K";
            }
            
    }

    public static void ascendente(String[] lista){
        traductorTexANum(lista);
        for(int i = 1; i < lista.length; i++) {
            int valorActual = lista[i];
            int j = i-1;
            while(j>=0 && lista.get(j) > valorActual){
                lista.set(j + 1, lista.get(j));
                j--;
            }
            lista.set(j+1, valorActual);
        }
    }

    public static void descendente(String[] lista){
        for(int i = 1; i < lista.length; i++) {
            int valorActual = lista[i];
            int j = i-1;
            while(j>=0 && lista.get(j) < valorActual){
                lista.set(j + 1, lista.get(j));
                j--;
            }
            lista.set(j+1, valorActual);
        }
    }
}
}