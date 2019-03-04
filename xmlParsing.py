import requests
import xml.etree.ElementTree as ET

# 농사로의 동영상 조회 rest api 연동
def sendRequest():
    
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    
    #query parameter
    params = {
        'apiKey': '',  #api key
        'subCategoryCode': 'FC010101',
        'pageNo': 1
    }
    
    # create http response object
    resp = requests.get('http://api.nongsaro.go.kr/service/cropTechInfo/videoList', headers = headers, params = params)

    # saving response to xml file
    with open('pageContent.xml', 'wb') as f:
        f.write(resp.content)
        
def parseXML(xmlfile):
    img, link, title, instt = [], [], [], []

    tree = ET.parse(xmlfile)

    root = tree.getroot()

    # get item element and children element(item/videoImg...)
    for item in root.iter('item'):
        for child in item:
            if child.tag == 'videoImg':
                img.append(child.text)
            elif child.tag == 'videoLink':
                link.append(child.text)
            elif child.tag == 'videoTitle':
                title.append(child.text)
            elif child.tag == 'videoOriginInstt':
                instt.append(child.text)


if __name__ == '__main__':
    sendRequest()
    parseXML('pageContent.xml')
