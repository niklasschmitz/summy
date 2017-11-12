import sys
import rake
import json
import Word, Sentence, compute_summary, visualisation

import plotly.plotly as py
from plotly.graph_objs import *

import networkx as nx


def getText(filepath):
    #open file and paste into text
    fp = open(filepath)
    text = fp.read()
    fp.close()

    return(text)


def getKeywords(text):
    ##new rake object
    rake_o = rake.Rake("SmartStoplist.txt", 2, 3, 4)
    ##filter out keywords
    keywords = rake_o.run(text)
    ##new array for keywords
    results = [""]*(len(keywords))

    ##iterate over array to extract keywords from tuple
    for i in range(0, len(keywords)):
        results[i] = str(keywords[i][0])

    return(results)

def splitUp(text):
    sentences = rake.split_sentences(text)
    sen = []
    for i in sentences:
    	sen.append(Sentence.Sentence(i))
    return (sen)

def createNodes(keywords):
    nodes = []
    for k in keywords:
        nodes.append({"keyname": k.id, "name": k.content, "size": k.occurency})
    return (nodes)

def linkNodes(sentences):
    links = []
    linkDicts = []
    occurency = []
    for s in sentences:
        for k in s.kw:
            for g in s.kw:
                if k.id > g.id:
                    l = (g,k)
                if k.id < g.id:
                    l = (k,g)
                else:
                    continue

                if l in links:
                    i = links.index(l)
                    occurency[i] += 1
                else:
                    links.append(l)
                    occurency.append(1)

    for l in range(0,len(links)):
        linkDicts.append({"source": links[l][0].id, "target": links[l][1].id, "width": occurency[l]})

    return(linkDicts)

def main(filepath):
    text = getText(filepath)
    keywords = getKeywords(text)
    kw = []
    for k in range(0,len(keywords)):
    	kw.append(Word.Word(k,keywords[k]))

    sentences = splitUp(text)

    #occurency = countOccurency(sentences, keywords)

    sentences,summ = compute_summary.compute_summary(sentences, kw, )
    nodes = createNodes(kw)
    links = linkNodes(sentences)
    graph = {"nodes": nodes, "links": links}
    visualisation.displayGraph(graph)

if __name__ == "__main__":
    main(sys.argv[1])
