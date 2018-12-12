from django.shortcuts import render
import operator
def Home(request):
    return render(request, 'home.html')

def Counter(request):
    content = request.GET["content"]
    content_length = len(content.split())
    word_counter = {}
    for word in content.split( ):
        if word in word_counter:
            word_counter[word] +=1
        else:
            word_counter[word] = 1

    sorted_words = sorted(word_counter.items(), key=operator.itemgetter(1), reverse = True)
    pk = {'content' : content, 'content_length' : content_length, 'word_list' : sorted_words,}
    return render(request, 'counter.html', pk)

def About(request):
    return render(request, 'about.html')
