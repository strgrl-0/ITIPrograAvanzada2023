package Humans.Soldiers;
import Humans.Soldier;

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
        Logistics currenLogistics = new Logistics(
            id,
            name,
            surname,
            nickname,
            specialization,
            soldier_value,
            distributedSupplies,
            attendedTroops
        );

        return currenLogistics;
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
