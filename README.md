Talk
====

Talk is a programming language with the following defining feature: functions can be declared to accept arguments at any place not just at the end, something like this:

    (argument1)functionName(argument2)
or

    GetFirst(2)ItemsIn(12, 2, 8, 33, 9)GreaterThan(10)
 
I have a belief that this feature alone can enable programs that are highly readable and expressive.
 
####Some design ideas####
Perhaps we can allow a function to be composed of interchangeable parts. For instance, in the example above, we can allow 'GreaterThan' to be substituted by 'LessThan' without the programmer having to declare two full declarations whose leading portions are identical. This will bring orthgonality to the design.

Also, could we get rid of those parenthesis? And may be we can allow spaces between words in the function name. That'll make the function call read like a sentence. For example:

    Get first 2 items in [12, 2, 8, 33, 9] greater than 10
 
####Object orientation####
We can have classes with methods in Talk, but we won’t be restricted to calling them in the prevalent way, which is:
    
    objectName.functionName(arguments…)
    
We are instead free to call them using Talk's peculiar syntax:
    
    AMethodOf(objectName)Taking(someArgument)ThatCanBeCalledInThis(“way”)
 
An interesting consequence of this is that the period ('.') is no longer used in method calls. So we’re free to repurpose it. What if we use it as a statement terminator? It would be especially interesting to combine it with the above “spaces in function name” syntax and produce a thoroughly natural language like syntax. For example:


    Get first 2 items in [12, 2, 8, 33, 9] greater than 10.
 
####Implementation####
When the compiler/interpreter encounters a function call, it starts matching it character by character with a trie of function declarations it knows about. If there's a match, it compiles the call. Else it raises an error.

####Target language####
Currently we're aiming to emit Python from the compiler. Alternatively, we could emit bytecode for some VM to run. Or, we could go the interpreter route. Let's see how it goes.
####Case sensitivity####
Talk should be case insensitive. That way, you can capitalize words in a function name, or keywords such as 'if', when they occur at the beginning of a 'sentence' and keep them all small otherwise.
