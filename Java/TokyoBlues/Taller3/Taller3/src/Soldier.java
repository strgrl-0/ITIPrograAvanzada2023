public abstract class Soldier extends StatHuman{

    private String nickname;
    private int soldier_value;

    //builder
    public Soldier(
    int id, 
    String name, 
    String surname, 
    String nickname, 
    String specialization, 
    int soldier_value
    ){
        super(id, name, surname, specialization);
        this.nickname = nickname;
        this.soldier_value = soldier_value;
    }


    //get

    public String getNickname() {
        return nickname;
    }

    public int getSoldier_value(){
        return soldier_value;
    }


    
}
