def LPSArray(pattern, lps):
    # Procedure to find longest prefix suffix
    # Parameter
        # pattern : string
        # lps : array of integer

    # Length of previous LPS
    length = 0

    # Length of pattern
    lenPattern = len(pattern)

    # the 0th lps is always 0
    lps[0] = 0
    idx = 1

    while (idx < lenPattern) :
        if (pattern[idx] == pattern[length]) :
            length += 1
            lps[idx] = length
            idx += 1
        else :
            if (length != 0):
                length = lps[length-1]
            else:
                lps[idx] = 0
                idx += 1

def KMPStringMatch(text, pattern):
    # Parameter
        # text      : string
        # pattern   : string
    # calculates array of lps that will holds the longest prefix suffix
    lps = [0] * len(pattern)
    LPSArray(pattern, lps)

    # length of pattern and text
    lenPattern = len(pattern)
    lenText = len(text)

    # index for text (i) and pattern (j)
    i = 0
    j = 0

    while (i < lenText):
        if (pattern[j] == text[i]):
            i += 1
            j += 1
        
        if (j == lenPattern) :
            # Pattern found at index i-j
            j = lps[j-1]
            return True
            
        # mismatch after j matches
        elif (i < lenText and pattern[j] != text[i]) :
            # Do not match with lps[0..lps[j-1]] but they will match anyway
            if (j != 0):
                j = lps[j-1]
            else :
                i += 1

    # Pattern not found
    return False




