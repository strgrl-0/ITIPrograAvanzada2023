
package Humans.Programmers;
import Humans.Programmer;
import Helpers.Abort;
import Helpers.Limiters;

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
        programmer_value = Limiters.calculateProgrammerValue(iaAlgorithmExperienceLevel, implementedAlgorithms);
        
        IaEngineer currentIaEngineer = new IaEngineer(id, 
        name, 
        surname, 
        specialization,
        programmer_value, 
        iaAlgorithmExperienceLevel, 
        implementedAlgorithms);

        //I KNOW THERE'S A BETTER WAY BUT IM NOT IN THE MOOD RN
    
        boolean isProgrammerLevelValid = Limiters.isProgrammerLevelValid(iaAlgorithmExperienceLevel);
        currentIaEngineer = (IaEngineer) Abort.delete(
            currentIaEngineer,
            isProgrammerLevelValid);

            
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
