package Humans.Soldiers;
import Humans.Soldier;
import Helpers.Limiters;

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
        soldier_value = Limiters.valuesLimiter(soldier_value);

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
