#### **<u>REGEX MODULE</u>**:-

```
- word boundary can be any non alphanumberic character not just only space including the bar before start of the character 
- but it should not be alphanumeric chars

- if we are going to group an existing expression in the regex it will not affect the existing match as we are covering the same with a group

- but it does provide an option to extract the group info from the regex using \(regex101/python) or $(atom) sign with corresponding group value which starts from 1 and goes onwards....

- python usage:-
	
    python r"<str with meta char>":-this will be considered as the raw string and will not allow metachar to escape unlike normal str as "<str with meta char>"

	Flags:-
	------------

-	we can provide the re.IGNORECASE or re.I as args to the compile() id we are using the pattern obj or other methods as args as re.IGNORECASE or re.I in order to ignore cases while matching   

- re.MULTILINE which can be provided same as re.I or re.IGNORECASE which will use the ^ or $ as the same way for multiple line text where each line should be start with designated pattern provided 

- re.VERBOSE used to provide comment and white space in pattern while re.compile() in order to deduce the regular pattern while explaining 

	
    finditer():-
    ------------------
    * finditer() on the pattern obj(re.compile(r"<pattern>")) or (re module with patter str and target str args) return an iterator which has span(start and end index) info and match cases which can be iterated and found
    * each item in the iterator having something called as the match object using the match.group(<group index >) we can fetch the indivual group value
    * but remember match.group(0) #return all the match
    * match.group(1) #return only the group1 value same goes for the rest
	
    findall():-
    -----------------
    *can be applied on pattern object (re.compile(f"<pattern>"))
    * can be applied as re.findall(patter,targetstr)
    * when we use the findall() it will return the list of matches only
    * but remeember when we use findall() and regular expression having group then findall() will return the list of tuple of  each group match not the enite match 
    * findall() will return the list of matched string if no group in the regex
    * but if findall() will return list of match as list contains tuple which contain each group match if grouping exist

	sub():-
    ---------------
    * can be applied on pattern object (re.compile(f"<pattern>"))
    * can be applied as re.findall(patter,"<replacevalue>,"targetstr)
    * used to return the replacement string in return
    
    subn():-
    -----------
    * can be applied on pattern object (re.compile(f"<pattern>"))
    * can be applied as re.findall(patter,"<replacevalue>,"targetstr)
    * same as sub() but along with replacement value it will return the number of replacement happend and return the value in the tuple format 
    
    match():-
    ----------------
    * can be applied on pattern object (re.compile(f"<pattern>"))
    * can be applied on the re  module as re.match(pattern,target func)
    #return the match object if pattern provided exist on start
    #else return None as value 
    
    fullmatch()
    ------------
    * can be applied on pattern object (re.compile(f"<pattern>"))
    * can be applied on the re  module as re.fullmatch(pattern,target func)
    #return the match object of pattern matches the target string fully
    #if not matches return the None as the return value 
    
    search()
    ---------
    * can be applied on pattern object (re.compile(f"<pattern>"))
    * can be applied on the re  module as re.search(pattern,target func)
    #search() return the match object based on the 1st match
    #if there were multiple matches also in that case search will only choose the 1st match return as match object 
    #if no match found then return the None Object 
    
    split()
    ----------
    * can be applied on pattern object (re.compile(f"<pattern>"))
    * can be applied on the re  module as re.split(pattern,target func)
    #split() devide the target dtring based on the pattern provided 
    #split() will return the list of string after the spit been occure
    #but we need to be careful about the . as we need to escape if not provided in the character set

```

