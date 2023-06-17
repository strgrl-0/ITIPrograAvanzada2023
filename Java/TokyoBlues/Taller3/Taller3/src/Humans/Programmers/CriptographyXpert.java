
package Humans.Programmers;
import Humans.Programmer;

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
