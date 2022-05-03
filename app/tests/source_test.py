import unittest
#from ..models import Sources
#from app.models import Sources

class SourcesTest(unittest.TestCase): #Test Class to test the behaviour of the Sources class
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources(
            "CNN News", 
            "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at CCNNews.com.", 
            "https://cnnnews.go.com/"
        )

    def test_init(self):
        self.assertEqual(self.new_source.name,"CNN News")
        self.assertEqual(self.new_source.description,"Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at CCNNews.com.")
        self.assertEqual(self.new_source.url,"https://cnnnews.go.com/")

if __name__ == "__main__":
    unittest.main()

from ..models import Sources    