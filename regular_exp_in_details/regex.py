import re #impoerting the re module
from typing import Any
pattern=re.compile(r"https?://(www\.)?(\w+\.\w+|\w+\.\w+)")
#open the file as url and fetching the url from there
data:Any=None
with open("url.txt","r",encoding="utf-8") as f:
    data = f.read()

#fetching the domain and top level domain from the file
#we can use the subn or sub method for the same 
#theses are called substitute back reference of the group 

# replace_value,replacement_quantity=re.subn(pattern,r"Group2:\2",data)
# print(replace_value)
# print(replacement_quantity)

#alternate approach:
# replace_value,replacement_quantity=pattern.subn(r"Group2:\1",data)
# print(replace_value)
# print(replacement_quantity)

#another alternate method match.group(<group index>) also capture the group from the regex
# iter_match=pattern.finditer(data)
# for match in iter_match:
#     # print(match.group(0))
#     # print(f"Group1:{match.group(1)}")
#     print(f"Group2:{match.group(2)}")

#using the findall() method see how many group been returned
matched_group=pattern.findall(data)
print(matched_group)