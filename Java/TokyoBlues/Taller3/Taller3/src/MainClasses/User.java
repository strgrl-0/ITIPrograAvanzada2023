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

    public static User create(String[] partsUser){
        String username = partsUser[0];
        String password = partsUser[1];
        String country = partsUser[2];
        String clearance = partsUser[3];

        
        User current = new User(
            username,
            password,
            country,
            clearance);
            
        boolean isClearanceValid = isClearanceValid(clearance);
        current = (User) Abort.delete(current, isClearanceValid);
        return current;
    }

    public static boolean isClearanceValid(String clearance){
        String[] validClearanceLevels = new String[2];
        validClearanceLevels[0] = "User";
        validClearanceLevels[1] = "Admin";
        boolean isValid = false;

        for(int i = 0; i<2; i++){
            if(validClearanceLevels[i].equals(clearance)){
                isValid = true;
                break;
            }else{
                isValid = false;
            }
        }

        if(isValid == false){
            System.out.println("CLEARANCE INVALID, SKIPPING");
        }
        return isValid; 
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

    //get
    public String getUsername(){
        return username;
    }

    public String getPassword(){
        return password;
    }

    public String getCountry(){
        return country;
    }

    public String getClearance(){
        return clearance;
    }

    //set
    public void setUsername(String username){
        this.username = username;
    }

    public void setPassword(String password){
        this.password = password;
    }
    
    public void setCountry(String country){
        this.country = country;
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
