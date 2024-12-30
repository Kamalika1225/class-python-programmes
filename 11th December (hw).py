#1.
class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def validate(self):
        if len(self.password) < 8:
            return "Invalid: Password must be at least 8 characters long."
        if not self.password[0].isupper():
            return "Invalid: The first character must be an uppercase letter."
        if not any(char.isupper() for char in self.password):
            return "Invalid: Password must have at least one uppercase letter."
        if not any(char.islower() for char in self.password):
            return "Invalid: Password must have at least one lowercase letter."
        if not any(char.isdigit() for char in self.password):
            return "Invalid: Password must have at least one digit."
        
        special_characters = "!@#$%^&*(),.?\":{}|<>"
        if not any(char in special_characters for char in self.password):
            return "Invalid: Password must have at least one special character."
        
        return "Valid: Password meets all the requirements."

password = input("Enter your password: ")
validator = PasswordValidator(password)
result = validator.validate()
print(result)



#2.
#2
class Textprocessor:
    def _init_(self, text):
        self.text = text  
    def splitintosentences(self):
        sentences=[]
        sentence=""
        for i in self.text:
            sentence+=i
            if i in ".!?":
                sentences.append(sentence.strip())
                sentence=""
        return sentences
        def process_sentence(self):
            sentences=self.splitintosentences()
            print("Processed Sentence")
            for sentence in sentences:
                wordcount=len(sentence.split())
                print(f"Sentence:{sentence},Word Count:{wordcount}")
inp=input("enter paragraph")
tex=Textprocessor(inp)
print("Split Sentences")
sentences=tex.splitintosentences()
for sentence in sentences:
    print(sentence)
            
