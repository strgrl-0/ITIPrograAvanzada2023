package Helpers;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import MainClasses.*;

public abstract class FileHandling {
    public static Object[] fileToObject(File file) throws FileNotFoundException{
        
        int  objectArrSize = determineArraySize(file);

        Object current = null;
        Object[] currentObjectArr = new Object[objectArrSize];
        int i = 0;
        
        String filename = fileName(file);
        filename = filename.toUpperCase();
        

        Scanner scanner = new Scanner(file);
        String fileLine = "";

        while(scanner.hasNextLine()){
            String[] fileLineParts = fileLine.split(",");

            System.out.println(fileLineParts+"      iteration2");
            System.out.println(filename+"           iteration2");

            current = sendToAproppiateMethod(fileLineParts, filename);
            currentObjectArr[i] = current;

            i++;
            fileLine = scanner.nextLine();
        }

        scanner.close();

        return currentObjectArr;
    }

    public static String fileName(File file){
        String filename = file.getName();
        return filename;
    }
    

    //FIXME: Code doesn't seem to recognize the filename-case condition, not sure why, 
    //it recognizes stats-country but there's another error too

    
    public static Object sendToAproppiateMethod(String[] fileLineParts, String filename){
        Object current = null;

        switch(filename){
            case "STATS-SOLDIER.TXT":
                System.out.println("iteration 3 ss");
                current = sendToStatHuman(fileLineParts);
                return current;
            case "STATS-PROGRAMMER.TXT":
                System.out.println("iteration 3 sp");
                current = sendToStatHuman(fileLineParts);
                return current;
            case "STATS-COUNTRY.TXT":
                System.out.println("iteration 3 sc");
                current = sendToStatCountry(fileLineParts);
            case "IA.TXT":
                System.out.println("iteration 3 AI");
                current = sendToIa(fileLineParts);
                return current;
            case "USERS.TXT":
                System.out.println("iteration 3 usr");
                current = sendToUser(fileLineParts);
                return current;
            default:
                System.out.println("File not Recognized");
                break;

        }
        return current;
    }

    public static Object sendToStatHuman(String[] fileLineParts){
        System.out.println(fileLineParts);
        
        Object current = StatHuman.createHumanFromString(fileLineParts);
        return current;
    }

    public static Object sendToUser(String[] fileLineParts){
        Object current = User.create(fileLineParts);
        return current;
    }

    public static Object sendToIa(String[] fileLineParts){
        Object current = Ia.create(fileLineParts);
        return current;
    }

    public static Object sendToStatCountry(String[] fileLineParts){
        Object current = StatCountry.create(fileLineParts);
        return current;
    }

    public static int determineArraySize(File file) throws FileNotFoundException{
        Scanner scanner  = new Scanner(file);
        String fileLine = "";
        int fileArraySize = 0;

        while(scanner.hasNextLine()){
            fileArraySize++;
            fileLine = scanner.nextLine();
        }
        scanner.close();

        return fileArraySize;

    }
}
