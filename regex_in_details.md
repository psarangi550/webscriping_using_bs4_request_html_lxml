### **<u>REGEX EXPRESSION</u>** 

```
-	There are few meta charactr are there in regular expression which              need to be escaped
	-----------------------------------------------------------------
    \^$[{()]\+*?| have special meaning in regular expression but if we              are looking for these character it need to be escaped by                       using the back slash i.e \ symbol
    
-  below are the one which has a particular meaning by using the meta             char which used to select individual patter
	----------------------------------------------------------------
	\w: will match [a-z][A-Z][0-9] and _
    \d: will match [0-9]
    .: will match everything without newline
    \s:-will match whitespace(new line ,space ,tab)
    
    below are called anchor:-matches based on position rather than                 literal value
    ----------------------------------------------------------------
-    \b:- word boundary i.e space will be there before or after
      :- space also counted as the word boundary along with literal one
     \B:- negative of \b i.e should not be a word boundary
    
    
      ex:--->ha haha
      \bha:-will select ha and first ha from haha because of word                           boundary on left
      \Bha:-will only select 2nd ha from haha word list 
      \bha\b:- will match only ha of the first as both the side                              boundary exist
    
-	^<char>:-will match the word at the beginning of the line
	 <char>$:-will match the word at the end of the line
     
-	**the below are called as an character set</u>** :-
	-----------------------------------------------------

     [char]:-matches any chars provided in the square bracket(like OR)
	 [^char]:-should not match any chars from the square bracket
     
     1* while using the character set we don't have to escape any                      character(but if we want we can escape as well)
     2* searches for each character individually
     3* - i.e dash has a special meaning in character set [] & need to                 escaped in the character set
     4* - means to specify a range of values in the regular expression                  when used inside the character in characterset
     	ex:- [4-7] means [4567] or [a-d] means [abcd]
     4.5*- otherwise it will be consider as - literally
     5* ^ is also a special meaning inside the character set and need                  to be escaped
     6* ^ negate the value provided inside the character set if used on                the first
     7* even though we have multiple character insude the character set                but still it will only match one character based upon                          the value provided to the character set
     8* in the character set we don't have to mention the | as each                    chars or range will behave as an or operator only


-	quantifier are below
	----------------------------
    quantifier helps in match one or more than one character at a time 
    *:- matches o or any number of character
    +:- matches at least one or more
    ?:- o or mt most 1
    {<no>}:- specified number of character
    {<min>,<max>}:-minimum and maximum character
     
-    grouping and or condition in/between grouping
	 ----------------------------------------------
     - charset is used to match one character at a time but using group               we can match multiple character
     - ():- used for grouping the regex
     - |:-used as the either or or conditon
     - group also used to search a particular term i.e set of char not                along with single char
     - group help us to match several different pattern
     - for the grouping we need the parenthesis i.e ()
     - if we have to mention the either or or we need to use | symbol
     - in the group we can mention a list of chars with or operator as 
     -(<char>|<char>|<char>|......) :-grouping with OR
     
- 	Most important points
	-----------------------------------------------------
     - group can be used to fetch a particular section of the matched                 regular expression
     - we reference the group by using the $ or \ symbol
     - when we have group the entire match belong to group 0
     - then group1 can be represented by $1(atom) or \1(regex 101)                    similarly for the rest of values as $2(in atom) or \2(in                       regex101) and etc....
     - we can also form a group by providing parenthesis to the existing              group as well so that both the inner group will combine and                    form a new group between them
```