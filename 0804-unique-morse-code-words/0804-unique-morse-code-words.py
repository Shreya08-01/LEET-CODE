class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.",
            "--.", "....", "..", ".---", "-.-", ".-..",
            "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        ]
        
        unique = set()
        
        for word in words:
            code = ""
            
            for ch in word:
                index = ord(ch) - ord('a')
                code += morse[index]
            
            unique.add(code)
        
        return len(unique)