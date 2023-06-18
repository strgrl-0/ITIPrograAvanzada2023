package Humans.Soldiers;
import Helpers.Abort;
import Helpers.Limiters;
import Humans.Soldier;

public class SpecOps extends Soldier{
    private int succesfulCovertMissions;
    private int totalMissions;
    private int obtainedResources;

    SpecOps(
        int id,
        String name,
        String surname,
        String nickname,
        String specialization,
        int soldier_value,
        int succesfulCovertMissions,
        int totalMissions,
        int obtainedResources
    ){
        super(id, name, surname, nickname, specialization, soldier_value);
        this.succesfulCovertMissions = succesfulCovertMissions;
        this.totalMissions = totalMissions;
        this.obtainedResources = obtainedResources;
    }

    public static SpecOps create(
        int id,
        String name,
        String surname,
        String nickname,
        String specialization,
        int soldier_value,
        int succesfulCovertMissions,
        int totalMissions,
        int obtainedResources
    ){
        SpecOps currentSpecOps = new SpecOps(
            id,
            name,
            surname,
            nickname,
            specialization,
            soldier_value,
            succesfulCovertMissions,
            totalMissions,
            obtainedResources
        );
        soldier_value = Limiters.valuesLimiter(soldier_value);
        
        return currentSpecOps;
    }


    @Override
    public String toString(){
        String toStringSpecOps = super.toString();
        toStringSpecOps = toStringSpecOps + +
                            succesfulCovertMissions + " " +
                            totalMissions + " " +
                            obtainedResources;
        return toStringSpecOps;
    }
}
