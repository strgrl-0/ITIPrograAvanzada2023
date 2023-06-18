package Humans.Soldiers;
import Humans.Soldier;
import Helpers.Abort;

public class Logistics extends Soldier{
    private int distributedSupplies;
    private int attendedTroops;
    
    public Logistics(
        int id,
        String name,
        String surname,
        String nickname,
        String specialization,
        int soldier_value,
        int distributedSupplies,
        int attendedTroops
    ){
        super(id, name, surname, nickname, specialization, soldier_value);
        this.distributedSupplies = distributedSupplies;
        this.attendedTroops = attendedTroops;
    }

    public static Logistics create(
        int id,
        String name,
        String surname,
        String nickname,
        String specialization,
        int soldier_value,
        int distributedSupplies,
        int attendedTroops
    ){
        Logistics currentLogistics = new Logistics(
            id,
            name,
            surname,
            nickname,
            specialization,
            soldier_value,
            distributedSupplies,
            attendedTroops
        );
        boolean isSoldierValueValid = Abort.valuesLimiter(soldier_value);
        currentLogistics = (Logistics) Abort.delete(currentLogistics, isSoldierValueValid);

        return currentLogistics;
    }


    @Override
    public String toString(){
        String toStringLogistics = super.toString();
        toStringLogistics = toStringLogistics + +
                            distributedSupplies + " " +
                            attendedTroops;
        return toStringLogistics;
    }
}
