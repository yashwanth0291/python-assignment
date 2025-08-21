dict={'ram':100,
      'alice':80,
      'ravi':75

}
student=input("enter the student's name :")
if student in dict:
      print("{}'s marks {}".format(student,dict[student]))
else:
      print("not found")