public class threatAnalyst extends Soldier{
    private String iaVulnerabilityIdentificationCapacity;
    private int threatsDetected;

    public threatAnalyst(int id, String name, String surname,
    String nickname, String specialization, int soldier_value,
    String iaVulnerabilityIdentificationCapacity, int threatsDetected){
        super(id, name, surname, nickname, specialization, soldier_value);
        this.iaVulnerabilityIdentificationCapacity = iaVulnerabilityIdentificationCapacity;
        this.threatsDetected = threatsDetected;
    }

    @Override
    public String toString() {
        String toPrint;
        toPrint = getUniqueId()+" "+getUniqueName()+" "+getUniqueSurname()+" "+
        getNickname()+" "+getUniqueSpecialization()+" "+getSoldier_value()+
        " "+iaVulnerabilityIdentificationCapacity+" "+threatsDetected;
    return toPrint;
    }
}
