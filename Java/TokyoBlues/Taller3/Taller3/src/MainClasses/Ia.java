package MainClasses;

import Helpers.Abort;

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

    public static Ia create(
        String iaName, 
        String iaClass, 
        int healthPoints){
        
        boolean skip = BaseHpLimiter(healthPoints);
        int totalHP = totalHealthPoints(healthPoints, iaClass);
        
        skip = TotalHpLimiter(totalHP);

        Ia current = new Ia(
            iaName,
            iaClass,
            totalHP);
        
        current = (Ia) Abort.delete(current, skip);

        return current;
        }


    public static int totalHealthPoints(
        int initialHealthPoints, 
        String iaClass){
            
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

    public static boolean TotalHpLimiter(int TotalHp){
        int maxTotalHp = 4994;
        if(TotalHp>maxTotalHp){
            String Error = "An Ai CANT have more than 4994 total HP";
            System.out.println(Error);
            return true;
        }else{
            return false;
        } 

    }

    public static boolean BaseHpLimiter(int baseHp){
        int maxBaseHp = 2000;
        if(baseHp>maxBaseHp){
            String Error = "An Ai CANT have more than 2000 base HP";
            System.out.println(Error);
            return true;
        }else{
            return false;
        }
    }

    @Override
    public String toString() {
        String toPrintIa;
        toPrintIa = iaName + " " +
                    iaClass + " " +
                    healthPoints;

        return toPrintIa;                
    }


}
