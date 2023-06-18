
package Humans.Programmers;
import Humans.Programmer;
import Helpers.Abort;

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

        boolean isProgrammerValueValid = Abort.valuesLimiter(programmer_value);
        currentIaEngineer = (IaEngineer) Abort.delete(currentIaEngineer, 
        isProgrammerValueValid);
        return currentIaEngineer;
        
        }
        

    public String toString() {
        String toPrintIaEngineer;
        toPrintIaEngineer =  super.toString() + 
                            iaAlgorithmExperienceLevel + " " +
                            implementedAlgorithms;
        
        return toPrintIaEngineer;
    } 
}
