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
        
        while (scanner.hasNextLine()){
            String[] fileLineParts = scanner.nextLine().strip().split(",");
            current = sendToAproppiateMethod(fileLineParts, filename);
            currentObjectArr[i] = current;
            i++;
        }

        scanner.close();
        return currentObjectArr;
    }

    public static String fileName(File file){
        String filename = file.getName();
        return filename;
    }
    
    
    public static Object sendToAproppiateMethod(String[] fileLineParts, String filename){
        Object current = null;

    
        switch(filename){
            case "STATS-SOLDIERS.TXT":
                current = sendToStatHuman(fileLineParts);
                return current;
            case "STATS-PROGRAMMERS.TXT":
                current = sendToStatHuman(fileLineParts);
                return current;
            case "STATS-COUNTRY.TXT": 
                current = sendToStatCountry(fileLineParts);
                return current;
            case "IA.TXT":
                current = sendToIa(fileLineParts);
                return current;
            case "USERS.TXT":
                current = sendToUser(fileLineParts);
                return current;
            default:
                System.out.println("File not Recognized");
                return current;

        }
        
    }

    public static Object sendToStatHuman(String[] fileLineParts){
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
        Scanner scanner1  = new Scanner(file);
        int fileArraySize = 0;

        while(scanner1.hasNextLine()){

            scanner1.nextLine().strip();
            fileArraySize++;
        }
        scanner1.close();

        return fileArraySize;

    }
}
