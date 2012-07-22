Talk
====

Talk is a programming language with the following defining feature: functions can accept arguments at any place not just at the end. Like this:

    (argument1)functionName(argument2)
Or this:

    GetFirst(2)ItemsIn(12, 2, 8, 33, 9)GreaterThan(10)
 
This syntax, I believe, can enable programs that are highly readable and expressive.

Talk is a work in progress.
 
####Some design ideas####
Perhaps a function can be composed of interchangeable parts. For instance, in the example above, we should be able to substitute 'GreaterThan' with 'LessThan' without the programmer having to declare two full declarations whose leading parts overlap. This will make things a lot orthogonal.

Also, we could get rid of those parenthesis. And perhaps allow spaces between words in the function name. That'll make the function call read like a sentence. For example:

    Get first 2 items in [12, 2, 8, 33, 9] greater than 10
 
####Object orientation####
We can have classes in Talk, but we won’t be restricted to calling their methods in the normal way, that is:
    
    objectName.functionName(arguments…)
    
We are instead free to call them using Talk's own peculiar syntax:
    
    AMethodOf(objectName)Taking(someArgument)ThatCanBeCalledInThis(“way”)
 
An interesting consequence is that the period ('.') is no longer used in method calls. So we’re free to repurpose it. What if we use it as a statement terminator? It would be especially interesting to combine it with the above “spaces in function name” syntax and produce a thoroughly natural language like syntax. For example:


    Get first 2 items in [12, 2, 8, 33, 9] greater than 10.
 
####Implementation####
When the compiler/interpreter encounters a function call, it starts matching it character by character with a trie of function declarations it knows about. If there's a match, it compiles the call. Else it raises an error.

####Target language####
Currently we're aiming to emit Python from the compiler. Alternatively, we could emit bytecode for some VM to run. Or, we could go the interpreter route. Let's see how it goes.
####Case sensitivity####
Talk should be case insensitive. That way, you can capitalize words in a function name, or keywords such as 'if', when they occur at the beginning of a 'sentence' and keep them all small otherwise.
