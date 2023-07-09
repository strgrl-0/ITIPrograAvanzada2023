import java.io.File;
import java.io.FileNotFoundException;

import Helpers.FileHandling;
import Login.MainLogin;
import Menu.Menu;
import Menu.Procedures.*;

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
        
        System.out.println(arrProgrammers[1]);
        System.out.println(arrSoldiers[1]);
        System.out.println(arrStatCountry[1]);
        System.out.println(arrIas[0]);
        System.out.println(arrUsers[0]);


        boolean processedClearance = MainLogin.Login(arrUsers);

        if(processedClearance == true){
            //ProceduresAdmin
        }else if(processedClearance == false){
            Menu MenuUsr = new Menu(arrUsers, arrProgrammers, arrSoldiers, arrStatCountry, arrIas); 
        }
        
    }
}
