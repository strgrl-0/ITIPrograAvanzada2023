public class criptographyXpert extends Soldier {
    private String criptographicAlgorithmKnowledge;
    private String xperienceLevelInDataSec;
    private int succesfulImplementations;
    private String obfuscationAbilityLevel;

    public criptographyXpert(int id, String name, String surname, String nickname, 
    String specialization, int soldier_value, String criptographicAlgorithmKnowledge,
    String xperienceLevelInDataSec, int succesfulImplementations,
    String obfuscationAbilityLevel){
        super(id, name, surname, nickname, specialization, soldier_value);
        this.criptographicAlgorithmKnowledge = criptographicAlgorithmKnowledge;
        this.xperienceLevelInDataSec = xperienceLevelInDataSec;
        this.succesfulImplementations = succesfulImplementations;
        this.obfuscationAbilityLevel = obfuscationAbilityLevel;
    }

    @Override
    public String toString() {
        String toPrint;
        toPrint = getUniqueId()+" "+getUniqueName()+" "+getUniqueSurname()+" "+
        getNickname()+" "+getUniqueSpecialization()+" "+getSoldier_value()+" "+criptographicAlgorithmKnowledge+
        " "+xperienceLevelInDataSec+" "+succesfulImplementations+" "+obfuscationAbilityLevel;
    return toPrint;
    }

}
