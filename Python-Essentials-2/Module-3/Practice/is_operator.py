class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
# {val : 0}
object_2 = SampleClass(2)
# {val : 2}
object_3 = object_1
# {val : 0}
object_3.val += 1
# {val : 1}

print(object_1 is object_2)     # False
print(object_2 is object_3)     # False
print(object_3 is object_1)     # True
print(object_1.val, object_2.val, object_3.val) # 1, 2, 1

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)
# True, False

# The results prove that object_1 and object_3 are same but string_1 and string_2 are not despite the contents being same.