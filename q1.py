def minSubseq(source, target):
    sourceChars = [False] * 26  # Initialize an array to keep track of characters in source
    for c in source:
        sourceChars[ord(c) - ord('a')] = True  # Set corresponding index to True if character is present in source
    
    for c in target:
        if not sourceChars[ord(c) - ord('a')]:  # If a character in target is not in source, return -1
            return -1
    
    m = len(source)
    sourceIterator = 0
    count = 0
    
    for c in target:
        if sourceIterator == 0:  # Start counting a new subsequence
            count += 1
        while source[sourceIterator] != c:  # Move the sourceIterator until it matches the character
            sourceIterator = (sourceIterator + 1) % m
            if sourceIterator == 0:  # If we reach the end, start counting a new subsequence
                count += 1
        sourceIterator = (sourceIterator + 1) % m  # Move to the next character in source
    
    return count


# Test cases
print(minSubseq("abc", "abcbc"))  # Output: 2
print(minSubseq("abc", "acdbc"))  # Output: -1
print(minSubseq("xyz", "xzyxz"))  # Output: 3
