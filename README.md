Talk
====

Talk is a programming language with one distinctive feature: functions accept arguments at any place not just at the end. While most languages require you to declare functions this way:

    FunctionName(argument1, argument2)

In Talk you can do it like this:

    (argument1)FunctionName(argument2)

###But what's the point?###
Consider a function that takes a list of integers and returns the first N items greater than a certain integer T. In most languages, you write it like this:
    
    GetFirstGreaterThan(N, intList, T)

You might choose a different name, but without additional comments or a peek inside the implementation, it is hard to make sense of what this function does.

Talk, on the other hand, lets you declare the same function this way:

    GetFirst(N)ItemsIn(intList)GreaterThan(T)
    
This declaration is so clear and direct you don't need any comments. It reads like comment itself. 

###Aparenthesia###
Talk makes parenthesis optional in function invocations (just as Ruby does). While you can call the above function like this:

    GetFirst(2)ItemsIn([2, 5, 1, 8, 0, 6, 3])GreaterThan(5)

it's so much easier on the eye when you let go of the parenthesis:

    GetFirst 2 ItemsIn [12, 2, 8, 33, 9] GreaterThan 10

###Exploding
As you can see, this call is starting to look a lot like an English sentence.
Talk is currently a work in progress.
 
####Some design ideas####
\- Perhaps a function can be composed of interchangeable parts. For instance, in the example above, we should be able to substitute 'GreaterThan' with 'LessThan' without the programmer having to declare two full declarations whose leading parts overlap. This will make for nice orthogonality.

\- Also, we could get rid of those parenthesis and perhaps allow spaces between words in the function name. That'll make the function call read like a sentence. For example:

    Get first 2 items in [12, 2, 8, 33, 9] greater than 10
\- Object orientation: we'll have classes in Talk, but we won’t have to call their methods like this:

    objectName.functionName(arguments…)

Instead, we are free to use Talk's own peculiar syntax:
    
    AMethodOf(objectName)Taking(someArgument)ThatCanBeCalledInThis(“way”)
 
An interesting consequence of this is that the period ('.') is no longer used in method calls. So we’re free to repurpose it. What if we use it as a statement terminator? It would be especially interesting to combine it with the above “spaces in function name” syntax and produce a thoroughly natural language like syntax. For example:

    Get first 2 items in [12, 2, 8, 33, 9] greater than 10.
 
####Implementation####
When the compiler/interpreter encounters a function call, it starts matching it character by character with a trie of function declarations it knows about. If there's a match, it compiles the call. Else it raises an error.

####Target language####
Currently we're aiming to emit Python from the compiler. Alternatively, we could emit bytecode for some VM to run. Or, we could go the interpreter route. Let's see how it goes.
####Case sensitivity####
Talk should be case insensitive. That way, you can capitalize words in a function name, or keywords such as 'if', when they occur at the beginning of a 'sentence' and keep them all small otherwise.
