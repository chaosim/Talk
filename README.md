Talk
====

Talk is a programming language with one distinctive feature: functions accept arguments at any place not just at the end. While most languages require you declare functions this way:

    FunctionName(argument1, argument2)

Talk lets you do it like this:

    (argument1)FunctionName(argument2)

###What's so great about that?###
Consider a function that takes a list of integers and returns the first N items greater than a certain integer T. In other languages, you'll write it like this:
    
    GetFirstGreaterThan(N, intList, T)

You might choose a different name, but it'll end up being just as cryptic. Without additional comments or a peek inside the implementation, it is hard to make sense of what this function does.

Talk, on the other hand, allows you to declare the same function so:

    GetFirst(N)ItemsIn(intList)GreaterThan(T)
    
This declaration is so clear and direct you don't need any comments. It reads like comment itself. 

What this means is that Talk doesn't force you into unnatural contortions when writing functions. As you'll see below, Talk's function invocation syntax reinforces this philosophy even further.

###Invocations###
#####Aparenthesia#####
Parenthesis are optional in when you invoke functions. So while you can call the above declared function like this:

    GetFirst(2)ItemsIn([2, 5, 1, 8, 0, 6, 3])GreaterThan(5)

it's so much easier on the eye if you leave parenthesis out:

    GetFirst 2 ItemsIn [12, 2, 8, 33, 9] GreaterThan 10

#####Exploding function names#####
Talk even allows you to insert spaces between words that make up a function name. So it's perfectly valid syntax if you wrote the above call this way instead:

    Get First 2 Items In [12, 2, 8, 33, 9] Greater Than 10

Seeing this statement, the Talk compiler/interpreter will intelligently try to match it with one of the function declarations it has seen before.

#####Case oblivious#####
Talk is a case insensitive language. So it lets you avoid the awkwardness of case in the preceding statement by letting you use a more natural capitalization. In other words, it's perfectly okay if you wrote the above like this:

    Get first 2 items in [12, 2, 8, 33, 9] greater than 10


####Classes and the period####
Talk supports object orientation but with one difference: you can't call methods on an object in the regular way:
    
    objectName.functionName(argument)

Instead you use Talk's own peculiar syntax:
    
    AMethodOf(objectName)TakingAn(argument)
    
An interesting consequence of this is that the period is freed up. So Talk goes ahead and repurposes it as the statement terminator. 

With the period append, the preceding function call now becomes:

    Get first 2 items in [12, 2, 8, 33, 9] greater than 10.
    
This is practically indistinguishable from an English sentence. (There could be an ambiguity while parsing real numbers because they contain a decimal. But that ambiguity can be resolved by noting that the tokens on both sides of the decimal must be strings of digits.) 


###Big picture###
The motivation behind talk is readability. It aims to be a language in which you can write programs that are so expressive that they are trivial to understand. It is partly inspired by Donald Knuth's [Literate Programming](http://en.wikipedia.org/wiki/Literate_programming) and the language Ruby. It also will borrow heavily from Python syntax-wise (indentation as block marker, for example, will be a nice idea for us).

Talk is currently a work in progress and is in an extremely early stage (actually, it's merely an idea right now) .
 

###Implementation###
How will we match an "exploded name" invocation with a function? When the compiler/interpreter encounters such a function call, it starts matching it character by character with a trie of function declarations it knows about. It ignores spaces as long as they are not around arguments. If there's a match, it compiles the call. Else it raises an error.

We're currently aiming to emit Python from the compiler. Eventually we'll take the interpreter route. Let's see how it goes.

###Some design ideas###
- Perhaps we can design a function to be composed of interchangeable parts. For instance, in the example above, we should be able to substitute 'GreaterThan' with 'LessThan' without the programmer having to declare two full declarations whose leading parts overlap. This will make for nice orthogonality.
- \<Add the next one here\>