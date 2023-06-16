
package Humans.Programmers;
import Humans.Programmer;

public class IaEngineer extends Programmer {
    
    private String iaAlgorithmExperienceLevel;
    private int implementedAlgorithms;

    public IaEngineer(int id, 
    String name, 
    String surname, 
    String specialization, 
    int programmer_value, 
    String iaAlgorithmExperienceLevel,
    int implementedAlgorithms){

        super(id, name, surname, specialization, programmer_value);
        this.iaAlgorithmExperienceLevel = iaAlgorithmExperienceLevel;
        this.implementedAlgorithms = implementedAlgorithms;
    }

    public static IaEngineer create(
    int id, 
    String name, 
    String surname,
    String specialization, 
    int programmer_value, 
    String iaAlgorithmExperienceLevel,
    int implementedAlgorithms
    ){

        IaEngineer currentIaEngineer = new IaEngineer(id, 
        name, 
        surname, 
        specialization,
        programmer_value, 
        iaAlgorithmExperienceLevel, 
        implementedAlgorithms);
        return currentIaEngineer;
        
        }
@Override
public String toString() {
    String toPrint;
    toPrint =   getUniqueId() + " " +
                getUniqueName() + " " +
                getUniqueSurname() + " " +
                getUniqueSpecialization() + " " +
                getProgrammerValue() + " " +
                iaAlgorithmExperienceLevel + " " +
                implementedAlgorithms + " ";
    return toPrint;
}
}
