package Humans.Soldiers;
import Helpers.Abort;
import Humans.Soldier;

public class Infantry extends Soldier{
    private int completeMissions;
    private String weapon;


    public Infantry(
        int id, 
        String name, 
        String surname, 
        String nickname, 
        String specialization,
        int Soldier_value,
        int completeMissions, 
        String weapon
        ){
            super(id, name, surname, nickname, specialization, Soldier_value);
            this.completeMissions = completeMissions;
            this.weapon = weapon;
        }
        
    public static Infantry create(
        int id, 
        String name, 
        String surname, 
        String nickname, 
        String specialization,
        int Soldier_value,
        int completeMissions, 
        String weapon
    ){
        Infantry currentInfantry = new Infantry(
            id, 
            name, 
            surname, 
            nickname, 
            specialization, 
            Soldier_value, 
            completeMissions, 
            weapon);
        boolean isSoldierValueValid = Abort.valuesLimiter(Soldier_value);
        currentInfantry = (Infantry) Abort.delete(currentInfantry, isSoldierValueValid);
    
        return currentInfantry;
    }


    @Override
    public String toString(){
        String toStringInfantry = super.toString();
        toStringInfantry = toStringInfantry +
                            completeMissions + " " +
                            weapon;
        return toStringInfantry;
    }
}
