
package Humans.Programmers;
import Humans.Programmer;
import Helpers.Abort;
public class CriptographyXpert extends Programmer {

    private String criptographicAlgorithmKnowledge;
    private String xperienceLevelInDataSec;
    private int succesfulImplementations;
    private String obfuscationAbilityLevel;

    public CriptographyXpert(
    int id, 
    String name, 
    String surname, 
    String specialization, 
    int programmerValue, 
    String criptographicAlgorithmKnowledge,
    String xperienceLevelInDataSec, 
    int succesfulImplementations,
    String obfuscationAbilityLevel
    ){

        super(id, name, surname, specialization, programmerValue);
        
        this.criptographicAlgorithmKnowledge = criptographicAlgorithmKnowledge;
        this.xperienceLevelInDataSec = xperienceLevelInDataSec;
        this.succesfulImplementations = succesfulImplementations;
        this.obfuscationAbilityLevel = obfuscationAbilityLevel;
    }

    public static CriptographyXpert create(
        int id,
        String name,
        String surname,
        String specialization,
        int programmerValue,
        String criptographicAlgorithmKnowledge,
        String xperienceLevelInDataSec,
        int succesfulImplementations,
        String obfuscationAbilityLevel
    ){
        CriptographyXpert currentCriptographyXpert = new CriptographyXpert(
            id,
            name,
            surname,
            specialization,
            programmerValue,
            criptographicAlgorithmKnowledge,
            xperienceLevelInDataSec,
            succesfulImplementations,
            obfuscationAbilityLevel
        );

        boolean areProgrammerLevelsValid = false;

        /*TODO: There's prolly a less clusterfuck way but i spent a while on this fucking thing to work
        and i just wanna move on lmfao*/

        areProgrammerLevelsValid = Abort.isProgrammerLevelValid(criptographicAlgorithmKnowledge);
        currentCriptographyXpert = (CriptographyXpert) Abort.delete(
            currentCriptographyXpert, 
            areProgrammerLevelsValid);

        areProgrammerLevelsValid = Abort.isProgrammerLevelValid(xperienceLevelInDataSec);
        currentCriptographyXpert = (CriptographyXpert) Abort.delete(
            currentCriptographyXpert, 
            areProgrammerLevelsValid);

        areProgrammerLevelsValid = Abort.isProgrammerLevelValid(obfuscationAbilityLevel);
        currentCriptographyXpert = (CriptographyXpert) Abort.delete(
            currentCriptographyXpert, 
            areProgrammerLevelsValid);

        return currentCriptographyXpert;
    }

    @Override
    public String toString() {
        String toPrintCriptographyXpert;
        toPrintCriptographyXpert =  super.toString() + 
                                    criptographicAlgorithmKnowledge + " " +
                                    xperienceLevelInDataSec + " " +
                                    succesfulImplementations + " " +
                                    obfuscationAbilityLevel;
        
        return toPrintCriptographyXpert;
    }
}
