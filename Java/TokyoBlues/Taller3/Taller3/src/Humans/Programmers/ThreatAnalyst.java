package Humans.Programmers;
import Humans.Programmer;
import Helpers.Abort;

public class ThreatAnalyst extends Programmer{
    private String iaVulnerabilityIdentificationCapacity;
    private int threatsDetected;

    public ThreatAnalyst(
    int id, 
    String name, 
    String surname,
    String specialization, 
    int programmerValue,
    String iaVulnerabilityIdentificationCapacity,
    int threatsDetected
    ){
        
        super(id, name, surname, specialization, programmerValue);
        this.iaVulnerabilityIdentificationCapacity = iaVulnerabilityIdentificationCapacity;
        this.threatsDetected = threatsDetected;
    }

    public static ThreatAnalyst create(
    int id, 
    String name, 
    String surname,
    String specialization,
    int programmerValue, 
    String iaVulnerabilityIdentificationCapacity,
    int threatsDetected
    ){

        ThreatAnalyst currentThreatAnalyst = new ThreatAnalyst(
        id,
        name,
        surname,
        specialization, 
        programmerValue,
        iaVulnerabilityIdentificationCapacity,
        threatsDetected
        );

        boolean isProgrammerValueValid = Abort.valuesLimiter(programmerValue);
        currentThreatAnalyst = (ThreatAnalyst) Abort.delete(currentThreatAnalyst, 
        isProgrammerValueValid);

        return currentThreatAnalyst;
    }

    public String toString() {
        String toPrintThreatAnalyst;
        toPrintThreatAnalyst =  super.toString() + 
                                iaVulnerabilityIdentificationCapacity + " " +
                                threatsDetected;
        return toPrintThreatAnalyst;
    }

}
