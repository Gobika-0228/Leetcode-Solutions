from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []
        
        # We only need to check offsets from 0 to word_len - 1
        for i in range(word_len):
            left = i
            window_count = Counter()
            count = 0
            
            # Slide a window of size total_len across s
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j : j + word_len]
                
                if word in word_count:
                    window_count[word] += 1
                    count += 1
                    
                    # If we have too many instances of 'word', shrink from the left
                    while window_count[word] > word_count[word]:
                        left_word = s[left : left + word_len]
                        window_count[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # If count matches total words, we found a concatenation
                    if count == num_words:
                        result.append(left)
                else:
                    # Invalid word: reset window
                    window_count.clear()
                    count = 0
                    left = j + word_len
                    
        return result
