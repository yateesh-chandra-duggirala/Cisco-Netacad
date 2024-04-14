'''
Scenario
We strongly encourage you to play with the code we've written for you, and make some (maybe even destructive) amendments. Feel free to modify any part of the code, but there is one condition - learn from your mistakes and draw your own conclusions.

Try to:

- minimize the number of print() function invocations by inserting the \n sequence into the strings
- make the arrow twice as large (but keep the proportions)
- duplicate the arrow, placing both arrows side by side
'''
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# minimizing the number of print() function invocations by inserting the \n sequence into the strings
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

# Make the arrow twice as large
print("     *       ")            
print("    * *      ")
print("   *"," *    ",sep=2*" ") 
print("  * ","  *   ",sep=2*" ")
print(" *  ","   *  ",sep=2*" ")
print("*** ","  *** ",sep=2*" ")
print("  * ","  *   ",sep=2*" ")
print("  * ","  *   ",sep=2*" ")
print("  **","***   ",sep=2*"*")

# duplicate the arrow, placing both arrows side by side
print("    *    "*2)
print("   * *   "*2)
print("  *   *  "*2)
print(" *     * "*2)
print("***   ***"*2)
print("  *   *  "*2)
print("  *   *  "*2)
print("  *****  "*2)
