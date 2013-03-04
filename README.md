Talk
====

Talk is a programming language with one defining feature: functions accept arguments at any place not just at the end. While most languages force you to declare functions this way:

    FunctionName(argument1, argument2)

Talk is happy to let you do it like this:

    (argument1)FunctionName(argument2)

###What's so great about that?###
Readability. 

Consider a function that returns the first N numbers from a list greater than a certain number T. Normally you'd end up with a hard to understand declaration like this:
    
    GetFirstGreaterThan(N, intList, T)
    
But with Talk you can declare the same function as below:

    GetFirst(N)ItemsIn(intList)GreaterThan(T)

which makes your intent unambigously clear.


###Invocations###
Talk takes this expressiveness further with its function invocation syntax which has the following features:

#####Aparenthesia#####
Parenthesis are optional when you invoke functions. So while the above-declared function can be called like this:

    GetFirst(2)ItemsIn([2, 5, 1, 8, 0, 6, 3])GreaterThan(5)

it's okay to leave parenthesis out and invoke it thus:

    GetFirst 2 ItemsIn [12, 2, 8, 33, 9] GreaterThan 10

#####Exploding function names#####
When you call a function you may insert spaces between words that make up the function's name. The above call, therefore, can be rewritten like this:

    Get First 2 Items In [12, 2, 8, 33, 9] Greater Than 10

Seeing this statement the the compiler/interpreter will intelligently try to ignore spaces and match the call with one of the function declarations it has encountered before.

#####Case obliviousness#####
Function invocations are case-insensitive. So the above call can be further modified to the one below which has a more natural case of an English sentence:

    Get first 2 items in [12, 2, 8, 33, 9] greater than 10


#####Classes and the period#####
Talk supports object orientation, but it doesn't let you call methods on an object in the normal way:
    
    object.method(argument)

Instead you must use Talk's own peculiar syntax:
    
    A method of object taking an argument
    

An interesting consequence of this is that the period is freed up. Talk, in its by now evident quest for naturalness, repurposes the period as a statementment terminator and the invocation becomes indistinguishable from an English sentence:


    Get first 2 items in [12, 2, 8, 33, 9] greater than 10.
    

###Big picture###
As you can guess, the primary motivation behind Talk is readability. It aims to be a language in which you can write programs that are so expressive that they are trivial to understand. It is partly inspired by Donald Knuth's [Literate Programming](http://en.wikipedia.org/wiki/Literate_programming). Talk's function call syntax (optional parenthesis) comes from Ruby. Eventually it will also borrow heavily from Python (indentation as block marker, for example, will fit nicely in the scheme of things).

As [Paul Graham once noted](http://paulgraham.com/langdes.html), brevity is a necessary quality for the success of a programming language. It would seem that Talk goes completely against this notion. But that's actually not true, because Talk does not _impose_ verbosity; it merely _allows_ it. So you are free to write and call functions in the traditional way, but sometimes a lot can be gained by shuffling your arguments around.

Also, you often don't know how good a tool is until you've actually built it and used it. So Talk is also an experiement that tries to find out how practical a syntax like this can be. It may well turn out to be good enough for general-purpose programming. Or, it might find a niche in areas such as executable specifications or DSLs.

Talk is currently a work in progress and is in an extremely early stage (actually, it's merely an idea right now) .

###Implementation###
Two big questions:

#####What's this thing going to compile to?#####
We're currently aiming to emit Python from the compiler. Eventually we should take the interpreter route. Let's see how it goes.

#####How will the compiler match an "exploded name" invocation with a function?######
*Preliminary idea*: when the compiler/interpreter encounters such a call, it starts matching it character by character with a trie of function declarations it knows about. It skips spaces as long as they are not around arguments. If there's a match, it compiles the call. Else it raises an error.

*A more realistic answer*: we'll have to try it and see what mechanism we can come up with.



###Some design ideas###
- Perhaps we can design a function to be composed of interchangeable parts. For instance, in the example above, we should be able to substitute 'GreaterThan' with 'LessThan' without the programmer having to declare two full declarations whose leading parts overlap. This will make for nice orthogonality.
- \<Add the next one here\>
