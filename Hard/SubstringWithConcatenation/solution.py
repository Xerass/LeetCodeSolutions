from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        concat_len = word_len * len(words)

        n = len(s)

        if concat_len > n:
            return []

        
        #try a mapping solution, each distinct word will be matched to an int
        distinct = {}
        next_id = 0
        for w in words:
            if w not in distinct:
                distinct[w] = next_id
                next_id += 1
        
        #for cases where small number of distinct words, would be faster for a counter else dict
        K = next_id
        if K <= 1000: #if small K list should be faster
            target = [0] * K
            for w in words:
                target[distinct[w]] += 1
            use_list = True
        else:
            # build a target mapping keyed by ids (not by strings) so later lookups use ids
            tmp = {}
            for w in words:
                wid = distinct[w]
                tmp[wid] = tmp.get(wid, 0) + 1
            target = tmp
            use_list = False

        
        result = []

        append_result = result.append
        W = len(words)
        #for each offset, create an array of ids for word aligned windows
        for offset in range(word_len):
            #converts s[offset] into an array of word ids
            ids = []
            end = n - word_len + 1
            get = distinct.get
            i = offset
            while i < end:
                substring = s[i:i+word_len]
                ids.append(get(substring, -1))
                i += word_len
            
            #perform a slinding window over ids
            left = 0
            current = [0] * K if use_list else {}
            matched = 0 

            for right, idv in enumerate(ids):
                if idv != -1:
                    if use_list:
                        current[idv] += 1
                        # if this inclusion exceeds target, shrink left until ok
                        while current[idv] > target[idv]:
                            lid = ids[left]
                            current[lid] -= 1
                            left += 1
                        if right - left + 1 == W:
                            # compute original string index = offset + left*L
                            append_result(offset + left * word_len)
                            # slide left one to continue searching for next
                            lid = ids[left]
                            current[lid] -= 1
                            left += 1
                    else:
                        current[idv] = current.get(idv, 0) + 1
                        while current[idv] > target[idv]:
                            lid = ids[left]
                            current[lid] -= 1
                            left += 1
                        if right - left + 1 == W:
                            append_result(offset + left * word_len)
                            lid = ids[left]
                            current[lid] -= 1
                            left += 1
                else:
                    # reset window
                    left = right + 1
                    if use_list:
                        # zero the used portion — faster to allocate new when K small
                        current = [0] * K
                    else:
                        current.clear()
        return result
