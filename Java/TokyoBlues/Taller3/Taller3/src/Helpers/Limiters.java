package Helpers;
import MainClasses.*;

public class Limiters {
    public static int valuesLimiter(int value){
        int maxValue = 999;
        
        if(value>maxValue){
            value = 999;
            return value;
        }else if(value<0){
            value = 0;
            return value;
        }else{
            return value;
        }
    }

    public static boolean isCountryRepeated(
        String country, 
        StatCountry countryObject){
            String countryObjCountryNameToStr = countryObject.getCountryName();
            if(country == countryObjCountryNameToStr){
                return true;
            }else{
                return false;
            }
        }
    
    public static boolean isProgrammerLevelValid(String level){
        String[] validLevels = new String[]{"Low", "Intermediate", "Advanced"};
        
        for(int i = 0; i<validLevels.length; i++){
            if(validLevels[i].equals(level)){
                return true;
            }
        }
        return false;
    }

    public static int calculateProgrammerValue(String level, int currentValue){
        int[] levelValues = new int[]{150, 300, 450};   //levelValues [0] = 150.Low; [1] = 300.Intermediate; [2] = 450.Advanced;
        String[] validLevels = new String[]{"Low", "Intermediate", "Advanced"}; //[0] = Low; [1] = Intermediate; [2] = Advanced;

        for(int i = 0; i<validLevels.length; i++){
            if(validLevels[i].equals(level)){
                currentValue = currentValue + levelValues[i];
            }
        }

        currentValue = valuesLimiter(currentValue);
        
        return currentValue;
    }
    
}
