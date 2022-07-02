import enum
## Cancel-Culture


class ClassificationLabel:
    def  __init__(self,value,type,wikidata_id=None):
        self.value = value
        self.type = type
        self.wikidata_id = wikidata_id
        
        

class CancelCultureType:
    alisoneroman = ClassificationLabel(0,"CancelCultureType")
    armiehammer  = ClassificationLabel(1,"CancelCultureType")
    bobbaffert  = ClassificationLabel(2,"CancelCultureType")
    carson_king  = ClassificationLabel(3,"CancelCultureType")
    dojacat = ClassificationLabel(4,"CancelCultureType")
    gabcake = ClassificationLabel(5,"CancelCultureType")
    ginacarano = ClassificationLabel(6,"CancelCultureType")
    goya = ClassificationLabel(7,"CancelCultureType")
    jamescharles = ClassificationLabel(8,"CancelCultureType")
    jimmyfallon  = ClassificationLabel(9,"CancelCultureType")
    jk_rowling  =  ClassificationLabel(10,"CancelCultureType")
    lana  =  ClassificationLabel(11,"CancelCultureType")
    Lin_Manuel  =  ClassificationLabel(12,"CancelCultureType")
    morgan_wallen  =  ClassificationLabel(13,"CancelCultureType")
    pepe_le_pew  =  ClassificationLabel(14,"CancelCultureType")
    pepsi  =  ClassificationLabel(15,"CancelCultureType")
    projared  =  ClassificationLabel(16,"CancelCultureType")
    sebastian_stan  =  ClassificationLabel(17,"CancelCultureType")
    seuss  =  ClassificationLabel(18,"CancelCultureType")
    shane_gillis  =  ClassificationLabel(19,"CancelCultureType")
    starbucks  =  ClassificationLabel(20,"CancelCultureType")
    UnburntWitch  =  ClassificationLabel(21,"CancelCultureType")

class CancelCulture:
    CancelCulture = ClassificationLabel(1,"CancelCulture")
    not_CancelCulture = ClassificationLabel(0,"CancelCulture")

### sentiment
class sentiment:
     negative = ClassificationLabel(0,"sentiment")
     neutral = ClassificationLabel(1,"sentiment")
     positive = ClassificationLabel(2,"sentiment")

class sarcasm:
    sarcastic = ClassificationLabel(1,"sarcasm")
    not_sarcastic = ClassificationLabel(0,"sarcasm")

class sarcasm_type:
    sarcastic_understatement = ClassificationLabel(0,"sarcasm_type")
    sarcastic_rhetorical_question = ClassificationLabel(1,"sarcasm_type")
    sarcastic_overstatement = ClassificationLabel(2,"sarcasm_type")
    sarcastic_satire = ClassificationLabel(3,"sarcasm_type")
    sarcastic_sarcasm = ClassificationLabel(4,"sarcasm_type")
    not_sarcastic = ClassificationLabel(5,"sarcasm_type")

class Emoji:
    pass



### EMOTIONAL

class Emotion(enum.Enum):
    Neutral =   ClassificationLabel(0,"Emotion")
    Sadness =   ClassificationLabel(1,"Emotion")
    Non_neutral =   ClassificationLabel(3,"Emotion")
    Anger =   ClassificationLabel(4,"Emotion")
    Joy =   ClassificationLabel(5,"Emotion")
    Fear =   ClassificationLabel(6,"Emotion")
    Surprise =   ClassificationLabel(7,"Emotion")
    Disgust =   ClassificationLabel(8,"Emotion")
    Admiration  =    ClassificationLabel(9,"Emotion")
    Amusement = ClassificationLabel(10,"Emotion")
    Annoyance = ClassificationLabel(11,"Emotion")
    Approval = ClassificationLabel(12,"Emotion")
    Caring = ClassificationLabel(13,"Emotion")
    Confusion = ClassificationLabel(14,"Emotion")
    Curiosity = ClassificationLabel(16,"Emotion")
    Desire = ClassificationLabel(17,"Emotion")
    Disappointment = ClassificationLabel(18,"Emotion")
    Disapproval = ClassificationLabel(19,"Emotion")
    Embarrassment = ClassificationLabel(20,"Emotion")
    Excitement = ClassificationLabel(21,"Emotion")
    Gratitude = ClassificationLabel(22,"Emotion")
    Grief = ClassificationLabel(23,"Emotion")
    Love = ClassificationLabel(24,"Emotion")
    Nervousness = ClassificationLabel(25,"Emotion")
    Optimism = ClassificationLabel(26,"Emotion")
    Pride = ClassificationLabel(27,"Emotion")
    Realization = ClassificationLabel(28,"Emotion")
    Relief = ClassificationLabel(29,"Emotion")
    Remorse = ClassificationLabel(30,"Emotion")
    Hatred = ClassificationLabel(31,"Emotion")
    Annoyed = ClassificationLabel(32,"Emotion")
    Furious = ClassificationLabel(33,"Emotion")
    Contempt = ClassificationLabel(34,"Emotion")

### HOPE

class Hope(enum.Enum):
    NoHope = ClassificationLabel(0,"Hope")
    Hope = ClassificationLabel(1,"Hope")

### HATE and ABUSIVE

class Hate(enum.Enum):
    NoHate = ClassificationLabel(0,"Hate")
    Hate = ClassificationLabel(1,"Hate")

class HateOrOffensive(enum.Enum):
    NULL = ClassificationLabel(0,"HateOrOffensive")
    Hate = ClassificationLabel(1,"HateOrOffensive")
    Offensive =ClassificationLabel(3,"HateOrOffensive")
    
class HateGroup(enum.Enum):
    Disaabley = ClassificationLabel(0,"HateGroup")
    Gender  = ClassificationLabel(1,"HateGroup")
    Origin = ClassificationLabel(2,"HateGroup")
    Other = ClassificationLabel(3,"HateGroup")
    Religion = ClassificationLabel(4,"HateGroup")

class HateAnnotator_Sentiment(enum.Enum):
    Hateful = ClassificationLabel(0,"Hateful")   
    Normal = ClassificationLabel(1,"Normal")  
    Disrespectful = ClassificationLabel(2,"Disrespectful")  
    Abusive = ClassificationLabel(3,"Abusive") 
    Offensive = ClassificationLabel(4,"Offensive") 
    
class HateAnnotator_Sentiment_annotator(enum.Enum):
    pass
class HateTargetClassType(enum.Enum):
    pass

class HateTargetClassType(enum.Enum):
    pass
class HateTargetType(enum.Enum):
    BiasedAttitude = 0
    ActOfBiasAndDiscrimination = 1
    ViolenceAndGenocide = 2

class HateTargetLabels(enum.Enum):
    IndividualSecondPerson = 0
    IndividualThirdPerson = 1
    Group = 2

class HateTargetClass(enum.Enum):
    African = 0
    Asian = 1
    Caucasian = 2
    Women = 3
    Homosexual = 4
    Islam = 5
    Jewish = 6
    Hispanic = 7
    Men = 8
    Refugee = 9
    Economic = 10
    Other = 11
    Disability = 12
    Minority = 13
    Transphobic = 14
    Christens = 15
    Immigrants = 16
    Refugees = 17
    Arabs = 18


### FACT CHECK helpers
class Currency(enum.Enum):
    Yes = 1
    No = 0
class AuthorityAuthor(enum.Enum):
    Yes = 1
    No = 0
class AuthorityPublisher(enum.Enum):
    Yes = 1
    No = 0
class AuthoritySponsor(enum.Enum):
    Yes = 1
    No = 0
class AuthoritySource(enum.Enum):
    Yes = 1
    No = 0
class AuthorityWhere(enum.Enum):
    Yes = 1
    No = 0
class Accuracy(enum.Enum):
    Emotion = 0
    Error_spelling = 1
    Error_grammar = 2
    Error_typographical = 3

class PurposeMain(enum.Enum):
    Informing = 0
    Teaching = 1
    Selling = 2
    Entertaining = 3
    Research = 4
    SelfGainingPurposes = 5

class PurposeSub(enum.Enum):
    Fact = 0
    Opinion = 1
    Propaganda = 2
    Political = 3
    Personal = 4
    Religious = 5
    Ideological_bias = 6

# RADAR
# Data
class Data(enum.Enum):
    pass
class Rationale(enum.Enum):
    Yes = 1
    No = 0
# Relevance
class Relevance(enum.Enum):
    Yes = 1
    No = 0

# DEEP FAKE
class DeepFake(enum.Enum):
    YES = 1
    NO = 0

class BiasPolitcal(enum.Enum):
    LEFT = 0
    LEFT_LEANS = 1
    Center = 2
    RIGHT_LEANS = 3
    RIGHT = 4

class Factual(enum.Enum):
    Conspiracy_Pseudoscience = 0
    QuestionableSources = 1
    ProScience = 2
    JournalistBias  = 3
    MembershipQuestions = 4

class BinaryFacts(enum.Enum):
    YES = 1
    NO = 0

class MuitValueFacts(enum.Enum):
    YES = 1
    NO = 0
# stance
class stance_abortion(enum.Enum):
    none = 1
    against = 0
    favor = 0

class atheism_abortion(enum.Enum):
    none = 1
    against = 0
    favor = 0

class stance_climate(enum.Enum):
    none = 1
    against = 0
    favor = 0

class stance_feminist(enum.Enum):
    none = 1
    against = 0
    favor = 0

class stance_hillary(enum.Enum):
    none = 1
    against = 0
    favor = 0

class stance_covid(enum.Enum):
    none = 1
    against = 0
    favor = 0

class DocFactCheck(enum.Enum):
    REFUTES = 0
    NOT_ENOUGH_INFO = 1
    SUPPORTS = 2

class FactCheck(enum.Enum):
    Fact  = 0
    NoFact = 1


class FactCheck(enum.Enum):
    Fact  = 0
    MostlyFalse = 1  
    HalfTrue = 1  
    MostlyTrue = 1  
    No_Fact = 1 
    
    
class topic(enum.Enum):
    pass

