def findContentChildren(g, s) -> int:
        
        g.sort()
        s.sort()

        child_p = 0
        cookie_p = 0

        while child_p < len(g) and cookie_p < len(s):
            if s[cookie_p] >= g[child_p]:
                child_p += 1
            cookie_p += 1
        return child_p