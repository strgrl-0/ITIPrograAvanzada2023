package MainClasses;
import Helpers.Abort;

public class User {
    private String username;
    private String password;
    private String country;
    private String clearance;

    public User(
        String username, 
        String password, 
        String country, 
        String clearance){

        this.username = username;
        this.password = password;
        this.country = country;
        this.clearance = clearance;
    }

    public static User create(
        String username, 
        String password, 
        String country, 
        String clearance){
        
        boolean isClearanceValid = isClearanceValid(clearance);
        
        User current = new User(
            username,
            password,
            country,
            clearance);
        
        current = (User) Abort.delete(current, isClearanceValid);
        return current;
    }

    public static boolean isClearanceValid(String clearance){
        String[] validClearanceLevels = new String[2];
        validClearanceLevels[0] = "User";
        validClearanceLevels[1] = "Admin";
        boolean isValid = false;

        for(int i = 0; i<2; i++){
            if(validClearanceLevels[i] == clearance){
                isValid = true;
                break;
            }else{
                isValid = false;
            }
        }

        return isValid;    //abort takes true for deletion
    }

    public static boolean isUsernameRepeated(
        String username, 
        User user){
            String userIdToCompare = user.username;
            if(userIdToCompare == username){
                return true;
            }else{
                return false;
            }
    }

    @Override
    public String toString(){
        String toPrintUser;
        toPrintUser = username + " " +
                        password + " " +
                        country + " " +
                        clearance;
        return toPrintUser;
    }

}
