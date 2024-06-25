class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_store = []
        t_store = []
        for i in s:
            if len (s_store)!=0:
                if i=='#':
                    s_store.pop()
                    continue
            elif i=='#':
                continue
            s_store.append(i)
        for i in t:
            if len (t_store)!=0:
                if i=='#':
                    t_store.pop()
                    continue
            elif i=='#':
                continue
            t_store.append(i)
        
        if s_store==t_store:
            return True
        else:
            return False
        