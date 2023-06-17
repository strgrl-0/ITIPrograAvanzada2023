package MainClasses;

public class Ia {
    private String iaName;
    private String iaClass;
    private int healthPoints;

    public Ia(
        String iaName, 
        String iaClass, 
        int healthPoints){

        this.iaName = iaName;
        this.iaClass = iaClass;
        this.healthPoints = healthPoints;
    }

    @Override
    public String toString() {
        String toPrintIa;
        toPrintIa = iaName + " " +
                    iaClass + " " +
                    healthPoints;

        return toPrintIa;                
    }

    public static Ia create(
        String iaName, 
        String iaClass, 
        int healthPoints){
            
        Ia current = new Ia(
            iaName,
            iaClass,
            totalHealthPoints(healthPoints, iaClass));
            
        return current;
    }

    public static int totalHealthPoints(int initialHealthPoints, String iaClass){
        int totalHP = 0;
        switch(iaClass){
            case "S+":
                totalHP = initialHealthPoints + 2994;
                break;
            case "S":
                totalHP = initialHealthPoints + 1994;
                break;
            case "A":
                totalHP = initialHealthPoints + 994;
                break;
            case "B":
                totalHP = initialHealthPoints + 452;
                break;
            case "C":
                totalHP = initialHealthPoints + 226;
                break;
            case "D":
                totalHP = totalHP + initialHealthPoints;
                break;
            default:
                System.out.println("Class Not Recognized");
                break;
        }
        return totalHP;
    }


}
