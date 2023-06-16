import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        String aaaaa = "1,pooferfish,mamawebo,IaEngineer,110,Low,34";
        String bbbbb = "1,pooferfish,mamawebo,ThreatAnalyst,110,Med,123";
        String ccccc = "1,pooferfish,mamawebo,CriptographyXpert,110,Low,Medium,4,High";
        String[] ll = new String[3];
        ll[0] = aaaaa;
        ll[1] = bbbbb;
        ll[2] = ccccc;

        StatHuman[] objects = new StatHuman[3];

        for(int i=0;i<3;i++){

            Scanner scan = new Scanner(ll[i]);

            String line = scan.nextLine();
            String[] lineParts = line.split(",");
            objects[i] = StatHuman.createHumanFromString(lineParts);

            System.out.println(objects[i]);
        }

    }
}
