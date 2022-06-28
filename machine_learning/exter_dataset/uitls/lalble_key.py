import enum
## Cancel-Culture

class CancelCultureType:
    alisoneroman = 0
    armiehammer  = 1
    bobbaffert  = 2
    carson_king  = 3
    dojacat = 4
    gabcake = 5
    ginacarano = 6
    goya = 7
    jamescharles = 8
    jimmyfallon  = 9
    jk_rowling  = 10
    lana  = 11
    Lin_Manuel  = 12
    morgan_wallen  = 13
    pepe_le_pew  = 14
    pepsi  = 15
    projared  = 16
    sebastian_stan  = 17
    seuss  = 18
    shane_gillis  = 19
    starbucks  = 20
    UnburntWitch  = 21

class CancelCulture:
    CancelCulture = 1
    not_CancelCulture = 0

### sentiment
class sentiment:
     negative=0
     neutral=0
     positive=0
class sarcasm:
    sarcastic = 1
    not_sarcastic = 0
class sarcasm_type:
    sarcastic_understatement = 0
    sarcastic_rhetorical_question = 1
    sarcastic_overstatement = 2
    sarcastic_satire = 3
    sarcastic_sarcasm = 4
    not_sarcastic = 5

class Emoji:
    pass



### EMOTIONAL

class Emotion(enum.Enum):
    Neutral = 0
    Sadness = 1
    Non_neutral = 3
    Anger = 4
    Joy = 5
    Fear = 6
    Surprise = 7
    Disgust = 8
    Admiration  = 9
    Amusement = 10
    Annoyance = 11
    Approval = 12
    Caring = 13
    Confusion = 14
    Curiosity = 16
    Desire = 17
    Disappointment = 18
    Disapproval = 19
    Embarrassment = 20
    Excitement = 21
    Gratitude = 22
    Grief = 23
    Love = 24
    Nervousness = 25
    Optimism = 26
    Pride = 27
    Realization = 28
    Relief = 29
    Remorse = 30
    Hatred = 31
    Annoyed = 32
    Furious = 33
    Contempt = 34

### HOPE

class Hope(enum.Enum):
    NoHope = 0
    Hope = 1

### HATE and ABUSIVE

class Hate(enum.Enum):
    NoHate = 0
    Hate = 1
class Hate(enum.Enum):
    NoHate = 0
    Hate = 1
    
class HateGroup(enum.Enum):
    Disaabley = 0
    Gender  = 1
    Origin = 2
    Other = 3
    Religion = 4

class HateAnnotator_Sentiment(enum.Enum):
    Hateful = 0
    Normal = 1
    Disrespectful = 2
    Abusive = 3
    Offensive = 4
    
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


class topic(enum.Enum):
    pass

