package Menu.Procedures;
import Helpers.Node.NodeSystem; 
import MainClasses.User;

public interface menuUsrProcedures extends menuInterface{
    public void showSoldierGallery(Object[] soldiersArr);
    public void showProgrammerGallery(Object[] programmersArr);
    public NodeSystem createTeam(Object[] programmersArr, Object[] soldiersArr);
    public void showHistory();
    public void changeProfile(User currentUser);
    public void showTop();
    public int fightAgainstAi(Object[] programmersArr, Object[] soldiersArr, Object[] aiArr);
}
