package MainClasses;

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

        User current = new User(
            username,
            password,
            country,
            clearance);

        return current;
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
