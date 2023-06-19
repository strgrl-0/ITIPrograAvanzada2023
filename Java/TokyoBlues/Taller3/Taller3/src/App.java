import java.io.File;
import java.io.FileNotFoundException;

import Helpers.FileHandling;
import Humans.*;
import MainClasses.*;

public class App {
    public static void main(String[] args) throws FileNotFoundException{
        File programmersFile = new File("src/Files/stats-programmers.txt");
        File soldiersFile = new File("src/Files/stats-soldiers.txt");
        File countriesFile = new File("src/Files/stats-country.txt");
        File iasFile = new File("src/Files/ia.txt");
        File usersFile = new File ("src/Files/users.txt");

        //call containers

        Object[] arrProgrammers = FileHandling.fileToObject(programmersFile);


    
        Object[] arrSoldiers = FileHandling.fileToObject(soldiersFile);



        Object[] arrStatCountry = FileHandling.fileToObject(countriesFile);


        Object[] arrIas = FileHandling.fileToObject(iasFile);



        Object[] arrUsers = FileHandling.fileToObject(usersFile);

        
        System.out.println(arrProgrammers[0]);
        System.out.println(arrSoldiers[0]);
        System.out.println(arrStatCountry[0]);
        System.out.println(arrIas[0]);
        System.out.println(arrUsers[0]);

    }
}
