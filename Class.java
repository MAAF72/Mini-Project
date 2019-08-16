package Dir.SubDir;

public class Class1 {
	private DataType1 Variable1;
	private DataType2 Variable2;
	private DataType3 Variable3;

	public Class1(DataType1 Variable1,DataType2 Variable2,DataType3 Variable3) {
		this.Variable1 = Variable1;
		this.Variable2 = Variable2;
		this.Variable3 = Variable3;
	}

	public DataType1 GetVariable1() {
		return this.Variable1;
	}

	public void SetVariable1(DataType1 Variable1) {
		this.Variable1 = Variable1;
	}

	public DataType2 GetVariable2() {
		return this.Variable2;
	}

	public void SetVariable2(DataType2 Variable2) {
		this.Variable2 = Variable2;
	}

	public DataType3 GetVariable3() {
		return this.Variable3;
	}

	public void SetVariable3(DataType3 Variable3) {
		this.Variable3 = Variable3;
	}
}
