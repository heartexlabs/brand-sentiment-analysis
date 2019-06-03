"""
"""
import optparse
import heartex

CONFIG="""<View>
  <Text name="txt-1" value="$news"></Text>
  <Choices name="chc-1" toName="txt-1">
    <Choice value="Relevant"></Choice>
    <Choice value="Not Relevant"></Choice>
  </Choices>
</View>"""


if __name__=="__main__":
    """
    """
    parser = optparse.OptionParser()
    
    parser.add_option('-t', '--token', action="store", dest="token", help="heartex token")
    parser.add_option('-i', '--input', action="store", dest="input", default="news.csv", help="input file name")
    
    options, args = parser.parse_args()
    
    project = heartex.create_project(**vars(options), label_config=CONFIG, name="Brand Filter Project")
    o
    print("Visit this link and label:")
    print("https://go.heartex.net/expert/projects/%d/editor/" % (project, ))