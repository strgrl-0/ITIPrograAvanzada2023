public class iaEngineer extends Soldier {
    
    private String iaAlgorithmExperienceLevel;
    private int implementedAlgorithms;

    public iaEngineer(int id, String name, String surname, String nickname, 
    String specialization, int soldier_value, String iaAlgorithmExperienceLevel,
    int implementedAlgorithms){

        super(id, name, surname, nickname, specialization, soldier_value);
        this.iaAlgorithmExperienceLevel = iaAlgorithmExperienceLevel;
        this.implementedAlgorithms = implementedAlgorithms;

    }


    @Override
    public String toString() {
        String toPrint;
        toPrint = getUniqueId()+" "+getUniqueName()+" "+getUniqueSurname()+" "+
        getNickname()+" "+getUniqueSpecialization()+" "+getSoldier_value()+" "+iaAlgorithmExperienceLevel+
        " "+implementedAlgorithms;
    return toPrint;
    }

}
