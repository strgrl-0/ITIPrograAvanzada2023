package Menu;

public class TopPlayers {
    private String playername;
    private int score;

    public TopPlayers(String playername, int score){
        this.playername = playername;
        this.score = score;
    }

    //set
    public void setPlayername(String playername){
        this.playername = playername;
    }

    public void setScore(int score){
        this.score = score;
    }
    
    //get
    public String getPlayername(){
        return playername;
    }

    public int getScore(){
        return score;
    }
}
