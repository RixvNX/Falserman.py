from bin import TypeChecker as TC
import random

# DEFINED VARIABLES
CHARSTRING = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz1234567890"
UPPER_ABCS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
LOWER_ABCS = "abcdefghijklmnopqrstuvwxyz"
NUMBER = "1234567890"
LASTNAME = ["Smith", "Jones", "Williams", "Brown", "Taylor", "Davis", "Wilson", "Evans", "Thomas", "Johnson"]
FIRSTNAME = ["Aaron", "Abel", "Abraham", "Adam", "Alva", "Alan", "Alex", "Alexander", "Apollo", "Andy", "Bert", "Bill", "Ben", "Bob", "Blake", "Bobby", "Brant", "Brad", "Caleb", "James", "Emma", "William", "Olivia", "Benjamin", "Ava", "Elijah", "Sophia", "Lucas", "Isabella", "Michael", "Charlotte", "Alexander", "Mia", "Ethan", "Amelia", "Daniel", "Harper", "Matthew", "Abigail", "Joseph", "Emily", "Samuel", "Elizabeth", "David", "Sofia", "Henry", "Avery", "Jackson", "Grace", "Sebastian", "Scarlett", "Aiden", "Victoria", "Gabriel", "Brooklyn", "Anthony", "Lily", "Carter", "Evelyn", "Andrew", "Hannah", "Liam", "Ella", "Noah", "Chloe", "Oliver", "Samantha", "Jacob", "Natalie", "Lucas", "Grace", "Michael", "Hannah", "Matthew", "Sarah", "Daniel", "Emily", "Henry", "Lily", "David", "Avery", "Benjamin", "Scarlett", "Samuel", "Zoe", "Jackson", "Brooklyn", "Elijah", "Aria", "William", "Eleanor", "Joseph", "Penelope", "James", "Addison", "Alexander", "Aubrey", "Sebastian", "Madison", "Logan", "Luna", "Mason", "Hazel", "Christopher", "Stella", "Dylan", "Maya", "Caleb", "Nora", "Ethan", "Eva", "Ryan", "Leah", "Nathan", "Victoria", "Isaac", "Audrey", "Luke", "Claire", "Aaron", "Alice", "Daniel", "Lucy", "Jonathan", "Bella", "Adam", "Aaliyah", "Thomas", "Gianna", "Connor", "Isabelle", "Joshua", "Sophie", "Christian", "Nova", "Eli", "Skylar", "Nathaniel", "Paisley", "Andrew", "Everly", "Robert", "Mila", "Anthony", "Layla", "Colton", "Elena", "Jack", "Gabriella", "Julian", "Violet", "Levi", "Naomi", "Owen", "Lydia", "Parker", "Sadie", "Wyatt", "Ruby", "Xavier", "Mackenzie", "Charles", "Quinn", "Jonathan", "Delilah", "Josiah", "Hannah", "Hudson", "Savannah", "Asher", "Penelope", "Jason", "Zoe", "Micah", "Alexa", "Ian", "Eleanor", "Vincent", "Aria", "Austin", "Scarlett", "Miles", "Stella", "Chase", "Bella", "Aaron", "Lily", "Adrian", "Nora", "Leo", "Emilia", "Colin", "Lucy", "Max", "Eva", "Gavin", "Leah", "Silas", "Victoria", "Tristan", "Audrey", "Zachary", "Claire", "Dominic", "Alice", "Bryan", "Hazel", "Camden", "Sophie", "George", "Nova", "Blake", "Skylar", "Carlos", "Paisley", "Peter", "Everly", "Alex", "Mila", "Grant", "Layla", "Jeremy", "Elena", "Landon", "Gabriella", "Brayden", "Violet", "Brian", "Naomi", "Kenneth", "Lydia", "Kyle", "Sadie", "Jace", "Ruby", "Jude", "Mackenzie", "Paul", "Quinn", "Derek", "Delilah", "Beckett", "Hannah", "Gage", "Savannah", "Dean", "Penelope", "Tucker", "Zoe", "Arthur", "Alexa", "Jake", "Eleanor", "Felix", "Aria", "Simon", "Scarlett", "Dawson", "Stella", "Ryder", "Bella", "Maddox", "Lily", "Theodore", "Nora", "Elias", "Emilia", "Andy", "Lucy", "Jesse", "Eva", "Elliot", "Leah", "Victor", "Victoria", "Spencer", "Audrey", "Brady", "Claire", "Maxwell", "Alice", "Troy", "Hazel", "Axel", "Sophie", "Ronan", "Nova", "Ezekiel", "Skylar", "Emmett", "Paisley", "Cody", "Everly", "Marco", "Mila", "Seth", "Layla", "Trevor", "Elena", "Jasper", "Gabriella", "Raymond", "Violet", "Joel", "Naomi", "Griffin", "Lydia", "Riley", "Sadie", "Evan", "Ruby", "Jared", "Mackenzie", "Shane", "Quinn", "Cameron", "Delilah", "Liam", "Emma", "Noah", "Olivia", "William", "Ava", "James", "Isabella", "Oliver", "Sophia", "Benjamin", "Mia", "Elijah", "Charlotte", "Lucas", "Amelia", "Henry", "Harper", "Alexander", "Evelyn", "Sebastian", "Abigail", "Samuel", "Emily", "Daniel", "Elizabeth", "Matthew", "Sofia", "David", "Avery", "Joseph", "Ella", "Carter", "Scarlett", "Owen", "Grace", "Wyatt", "Chloe", "John", "Victoria", "Jack", "Lily", "Luke", "Hannah", "Jayden", "Natalie", "Dylan", "Layla", "Grayson", "Zoe", "Levi", "Penelope", "Isaac", "Riley", "Gabriel", "Brooklyn", "Julian", "Everly", "Mateo", "Leah", "Anthony", "Stella", "Jaxon", "Hazel", "Lincoln", "Ellie", "Joshua", "Paisley", "Christopher", "Audrey", "Andrew", "Skylar", "Theodore", "Violet", "Caleb", "Claire", "Ryan", "Bella", "Asher", "Aurora", "Nathan", "Lucy", "Thomas", "Anna", "Leo", "Savannah", "Isaiah", "Samantha", "Charles", "Caroline", "Josiah", "Genesis", "Hudson", "Aaliyah", "Christian", "Kennedy", "Hunter", "Kinsley", "Connor", "Maya", "Eli", "Valentina", "Ezra", "Naomi", "Aaron", "Alice", "Landon", "Sarah", "Adrian", "Eleanor", "Jonathan", "Eliana", "Nolan", "Sadie", "Jeremiah", "Piper", "Easton", "Lydia", "Elias", "Alexa", "Colton", "Josephine", "Cameron", "Adeline", "Carson", "Delilah", "Robert", "Serenity", "Angel", "Ariana", "Maverick", "Mila", "Nicholas", "Brielle", "Dominic", "Willow", "Jaxson", "Elise", "Greyson", "Gianna", "Adam", "Quinn", "Ian", "Clara", "Austin", "Everleigh", "Santiago", "Isla", "Jordan", "Ivy", "Cooper", "Haven", "Brayden", "Elena", "Roman", "Emery", "Evan", "Annabelle", "Ezekiel", "Daniela", "Xavier", "Harmony", "Jose", "Adalynn", "Jace", "Katherine", "Jameson", "Julia", "Leonardo", "Maddison", "Bryson", "Alexandra", "Axel", "Delaney", "Everett", "Kylie", "Parker", "Faith", "Kayden", "Brianna", "Miles", "Luna", "Sawyer", "Vivian", "Jason", "Camila", "Declan", "Sophie", "Weston", "Makayla", "Micah", "Madeline", "Ayden", "Willow", "Wesley", "Genesis", "Luca", "Scarlett", "Vincent", "Kinsley", "Damian", "Autumn", "Zachary", "Nevaeh", "Silas", "Nora", "Gavin", "Peyton", "Chase", "Serenity", "Kai", "Paisley", "Emmett", "Brooke", "Harrison", "Aubree", "Nathaniel", "Aliyah", "Kingston", "Lucia", "Cole", "Adeline", "Tyler", "Michelle", "Bennett", "Eliana", "Bentley", "Londyn", "Ryker", "Angelina", "Tristan", "Rylee", "Brandon", "Raelyn", "Kevin", "Liliana", "Luis", "Maria", "George", "Hadley", "Ashton", "Melanie", "Rowan", "Reagan"]
MAIL_NAMELENGHT = [7, 8, 9, 10, 11, 12]
MAIL_INCNAME = ["gmail", "yahoo", "hotmail", "outlook", "qq", "163"]
MAIL_INCM = [".com"]


class Spawner:
    def name(count:int) -> list:
        if TC.isInt(count) == False:
            return [f"{random.choice(FIRSTNAME)} {random.choice(LASTNAME)}"]
        Result = []
        for i in range(count):
            Result.append(f"{random.choice(FIRSTNAME)} {random.choice(LASTNAME)}")
        return Result
    
    def mail(count:int, lenght:int=0, inc:str="<NoInc>") -> list:
        Result = []
        __mailIncName = inc
        __names = ""
        if TC.isInt(lenght) == False:
            return ["ExampleTest@gmail.com"]
        if inc == "<NoInc>":
            __mailIncName = random.choice(MAIL_INCNAME)
        for i in range(count):
            if lenght != 0:
                for j in range(lenght):
                    __names += random.choice(CHARSTRING)
            else:
                for j in range(random.choice(MAIL_NAMELENGHT)):
                    __names += random.choice(CHARSTRING)
            Result.append(f"{__names}@{random.choice(MAIL_INCNAME)}{random.choice(MAIL_INCM)}")
        return Result
