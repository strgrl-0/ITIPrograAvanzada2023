public class App {
    public static void main(String[] args) throws Exception {
        Soldier aaaa = Soldier.createIaEngineer(0, null, null,
         null, null,
         0, null, 0);
        Soldier bbbb = Soldier.createThreatAnalyst(00, null, null, null,
        null, 0,
        "low", 01);

        Soldier cccc = Soldier.createCriptographyXpert(0, "aaa", "aaacc",
        null, null, 0, null,
        null, 0, null);
        
        System.out.println(aaaa);
        System.out.println(bbbb);
        System.out.println(cccc);
    }
}
