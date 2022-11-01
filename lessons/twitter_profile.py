"""Examples of Object-oriented Programming"""


class Profile:
    """An example of a somple social media profile model"""
    handle: str
    followers: int 
    is_private: bool 

    def __init__(self, handle: str):
        """Initializes all atributes of an object."""
        self.handle = handle 
        self.followers = 0 
        self.is_private = False
        
    def tweet(self, message: str) -> None: 
        print("@" + (self.handle) + " tweets " + (message))
            
            
my_profile: Profile = Profile("GMRTE720")
my_profile.tweet("'L bozo!'")

