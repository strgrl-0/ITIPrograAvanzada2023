package personClass;

public class Person {
	private String name;
	private String rut;
	private String password;
	private String clearance;
	
	public Person(String name, String rut, String password, String clearance) {
		this.name = name;
		this.rut = rut;
		this.password = password;
		this.clearance = clearance;
	}
	
	//getters & setters
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getRut() {
		return rut;
	}

	public void setRut(String rut) {
		this.rut = rut;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getClearance() {
		return clearance;
	}

	public void setClearance(String clearance) {
		this.clearance = clearance;
	}
	
}
