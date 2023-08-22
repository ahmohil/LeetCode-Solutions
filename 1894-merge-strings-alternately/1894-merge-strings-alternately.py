class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        sortedstring = ""
        if (len(word1) < len(word2)):
            for i in range(len(word1)):
                sortedstring += word1[i]
                sortedstring += word2[i]
            
            for i in range(len(word1),len(word2)):
                sortedstring += word2[i]
        else:
            for i in range(len(word2)):
                sortedstring += word1[i]
                sortedstring += word2[i]
            for i in range(len(word2),len(word1)):
                sortedstring += word1[i]

        return sortedstring
