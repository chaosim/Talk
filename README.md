Talk
====

Talk is a programming language with one defining feature: functions accept arguments at any place not just at the end. While most languages require you to declare functions like this:

    FunctionName(argument1, argument2)

Talk is happy to let you do it this way:

    (argument1)FunctionName(argument2)

###What's so great about that?###
Consider a function that takes a list of integers and returns the first N items greater than a certain integer T. In other languages, you'll have to write:
    
    GetFirstGreaterThan(N, intList, T)

This is very hard to make sense of without additional comments or a peek into the implemention.

With Talk, you can declare the same function like this:

    GetFirst(N)ItemsIn(intList)GreaterThan(T)
    
Clear and direct. You don't need any comments. The declaration practically reads like a comment itself. 

So this is what's good about this syntax: you're not forced into unnatural contortions to get your intent across. This makes for programs that are readable and expressive. As you'll see below, Talk's function invocation syntax reinforces this even further.

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
    
Now an interesting consequence of this is that the period is freed up. So Talk goes ahead and it as the statement terminator. 

With the period at the end, the preceding function call now becomes practically indistinguishable from an English sentence:

    Get first 2 items in [12, 2, 8, 33, 9] greater than 10.
    
Nice, isn't it?

###Big picture###
As you can guess, the primary motivation behind talk is readability. It aims to be a language in which you can write programs that are so expressive that they are trivial to understand. It is partly inspired by Donald Knuth's [Literate Programming](http://en.wikipedia.org/wiki/Literate_programming) and the language Ruby. It also will borrow heavily from Python syntax-wise (indentation as block marker, for example, will fit nicely in the scheme of things).

Talk is currently a work in progress and is in an extremely early stage (actually, it's merely an idea right now) .
 

###Implementation###
How will we match an "exploded name" invocation with a function? When the compiler/interpreter encounters such a function call, it starts matching it character by character with a trie of function declarations it knows about. It ignores spaces as long as they are not around arguments. If there's a match, it compiles the call. Else it raises an error.

We're currently aiming to emit Python from the compiler. Eventually we'll take the interpreter route. Let's see how it goes.

###Some design ideas###
- Perhaps we can design a function to be composed of interchangeable parts. For instance, in the example above, we should be able to substitute 'GreaterThan' with 'LessThan' without the programmer having to declare two full declarations whose leading parts overlap. This will make for nice orthogonality.
- \<Add the next one here\>