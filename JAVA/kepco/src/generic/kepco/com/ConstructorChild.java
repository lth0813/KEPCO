package generic.kepco.com;

public class ConstructorChild extends ConstructorParent{
	
//	상속 관계에서는 부모 상속자가 먼저 올라감(super())
	public ConstructorChild() {
		super();
		System.out.println("자식");
	}

	public static void main(String[] args) {
		ConstructorChild cc = new ConstructorChild();
		
	}
	
}
