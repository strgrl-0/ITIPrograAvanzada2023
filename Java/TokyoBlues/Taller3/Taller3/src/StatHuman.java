public abstract class StatHuman {
    private int uniqueId;
    private String uniqueName;
    private String uniqueSurname;
    private String uniqueSpecialization;

    //builder
    public StatHuman(int id, String name, String surname, 
    String specialization){
        this.uniqueId = id; this.uniqueName = name;
        this.uniqueSurname = surname; this.uniqueSpecialization = specialization;
    }

    //calls


    public static iaEngineer createIaEngineer(int id, String name, String surname, String nickname, 
    String specialization, int soldier_value, String iaAlgorithmExperienceLevel, 
    int implementedAlgorithms){
        
        iaEngineer currentIaEngineer = new iaEngineer(id, name, surname, nickname, 
        specialization, soldier_value, iaAlgorithmExperienceLevel, implementedAlgorithms);

        return currentIaEngineer;
    }

    public static threatAnalyst createThreatAnalyst(int id, String name, String surname, String nickname,
    String specialization, int soldier_value, String iaVulnerabilityIdentificationCapacity,
    int threatsDetected){

        threatAnalyst currentThreatAnalyst = new threatAnalyst(id, name, surname, nickname, specialization,
        soldier_value, iaVulnerabilityIdentificationCapacity, threatsDetected);

        return currentThreatAnalyst;
    }

    public static criptographyXpert createCriptographyXpert(int id, String name, String surname, String nickname, 
    String specialization, int soldier_value, String criptographicAlgorithmKnowledge,
    String xperienceLevelInDataSec, int succesfulImplementations,
    String obfuscationAbilityLevel){
        
        criptographyXpert currentCriptographyXpert = new criptographyXpert(id, name, surname, nickname,
        specialization, soldier_value, criptographicAlgorithmKnowledge, xperienceLevelInDataSec,
        succesfulImplementations, obfuscationAbilityLevel);

        return currentCriptographyXpert;
    }


    //set get
    public int getUniqueId(){
        return uniqueId;
    }

    public String getUniqueName(){
        return uniqueName;
    }

    public String getUniqueSurname(){
        return uniqueSurname;
    }

    public String getUniqueSpecialization(){
        return uniqueSpecialization;
    }

}
