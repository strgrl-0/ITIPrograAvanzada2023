package Humans.Soldiers;
import Helpers.Abort;
import Humans.Soldier;
import Helpers.Limiters;


public class Artillery extends Soldier{
    private int destroyedTargets;
    private float accuracy;

    public Artillery(
    int id,
    String name,
    String surname,
    String nickname,
    String specialization,
    int soldier_value,
    int destroyedTargets,
    float accuracy
    ){
        super(id, name, surname, nickname, specialization, soldier_value);
        this.destroyedTargets = destroyedTargets;
        this.accuracy = accuracy;
    }

    public static Artillery create(
        int id, 
        String name,
        String surname,
        String nickname,
        String specialization,
        int soldier_value,
        int destroyedTargets,
        float accuracy
    ){
        Artillery currentArtillery = new Artillery(
            id, 
            name, 
            surname, 
            nickname, 
            specialization, 
            soldier_value, 
            destroyedTargets, 
            accuracy);

            soldier_value = Limiters.valuesLimiter(soldier_value);

        return currentArtillery;
    }


    @Override
    public String toString(){
        String toStringArtillery = super.toString();
        toStringArtillery = toStringArtillery + +
                            destroyedTargets + " " +
                            accuracy;
        return toStringArtillery;
    }
}
