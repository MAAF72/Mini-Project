Package = ["Dir", "SubDir"]
ClassName = "Class1"
Variables = [["DataType1", "Variable1"],
			["DataType2", "Variable2"],
			["DataType3", "Variable3"]]

print("package {};".format('.'.join(Package)))

print()

print("public class {} {}".format(ClassName, '{'))

#Create Attribute
for v in Variables :
	print("\tprivate {} {};".format(v[0], v[1]))

print()

#Create Constructor
Constructor = ','.join([str(v[0] + " " + v[1]) for v in Variables])
print("\tpublic {}({}) {}".format(ClassName, Constructor, '{'))

for v in Variables :
	print("\t\tthis.{} = {};".format(v[1], v[1]))
	
print("\t}")

#Create Getter and Setter Method
for v in Variables :

	print()
	print("\tpublic {} Get{}() {}".format(v[0], v[1], '{'))
	print("\t\treturn this.{};".format(v[1]))
	print("\t}")
	
	print()
	print("\tpublic void Set{}({} {}) {}".format(v[1], v[0], v[1], '{'))
	print("\t\tthis.{} = {};".format(v[1], v[1]))
	print("\t}")
	
print("}")