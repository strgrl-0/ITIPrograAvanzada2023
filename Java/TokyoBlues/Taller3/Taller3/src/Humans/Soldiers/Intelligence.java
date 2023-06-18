package Humans.Soldiers;
import Humans.Soldier;
import Helpers.Abort;

public class Intelligence extends Soldier{
    private int collectedIntelligenceReports;
    private int identifiedEnemies;

    public Intelligence(
    int id,
    String name,
    String surname,
    String nickname,
    String specialization,
    int soldier_value,
    int collectedIntelligenceReports,
    int identifiedEnemies
    ){
        super(id, name, surname, nickname, specialization, soldier_value);
        this.collectedIntelligenceReports = collectedIntelligenceReports;
        this.identifiedEnemies = identifiedEnemies;
    }

    public static Intelligence create(
        int id,
        String name,
        String surname,
        String nickname,
        String specialization,
        int soldier_value,
        int collectedIntelligenceReports,
        int identifiedEnemies
    ){
        Intelligence currentIntelligence = new Intelligence(
            id,
            name,
            surname,
            nickname,
            specialization,
            soldier_value,
            collectedIntelligenceReports,
            identifiedEnemies
            );
            boolean isSoldierValueValid = Abort.valuesLimiter(soldier_value);
            currentIntelligence = (Intelligence) Abort.delete(currentIntelligence, 
            isSoldierValueValid);

        return currentIntelligence;
    }


    @Override
    public String toString(){
        String toStringIntelligence = super.toString();
        toStringIntelligence = toStringIntelligence + +
                            collectedIntelligenceReports + " " +
                            identifiedEnemies;
        return toStringIntelligence;
    }
}