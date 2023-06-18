import java.util.Scanner;
import MainClasses.*;
public class App {
    public static void main(String[] args) throws Exception {

        String aaaaa = "1,pooferfish,mamawebo,IaEngineer,110,Low,34";
        String bbbbb = "1,pooferfish,mamawebo,ThreatAnalyst,110,Intermediate,123";
        String ccccc = "1,pooferfish,mamawebo,CriptographyXpert,110,Low,Intermediate,4,Advanced"; 

        String a1 = "1,pooferfish,mamawebo,elgluglu,Artillery,100,40,99.2";
        String a2 = "1,pooferfish,mamawebo,elgluglu,Infantry,100,20,LEW";
        String a3 = "1,pooferfish,mamawebo,elgluglu,Intelligence,100,11,999";
        String a4 = "1,pooferfish,mamawebo,elgluglu,SpecOps,100,78,80,900000";
        String a5 = "1,pooferfish,mamawebo,elgluglu,Logistics,100,100000,200";

        String[] ll = new String[8];
        ll[0] = aaaaa;
        ll[1] = bbbbb;
        ll[2] = ccccc;
        ll[3] = a1;
        ll[4] = a2;
        ll[5] = a3;
        ll[6] = a4;
        ll[7] = a5;

        StatHuman[] objects = new StatHuman[8];

        for(int i=0;i<8;i++){

            Scanner scan = new Scanner(ll[i]);

            String line = scan.nextLine();
            String[] lineParts = line.split(",");
            objects[i] = StatHuman.createHumanFromString(lineParts);

            System.out.println(objects[i]);
        }

        //test Ia
        System.out.println(Ia.create("alto", "S+", 200));

        //test User
        System.out.println(User.create("Gabe", "marico1265", "Italia", "User"));
        //test country
        System.out.println(StatCountry.create("Chile", 17000000, 15000000, 385, 3500000));

    }
}
