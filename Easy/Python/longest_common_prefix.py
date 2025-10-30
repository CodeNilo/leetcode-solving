class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        
        prefix = strs[0]

        new_list = strs[1:]


        for i in range(len(new_list)):
            while not new_list[i].startswith(prefix):

                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix
