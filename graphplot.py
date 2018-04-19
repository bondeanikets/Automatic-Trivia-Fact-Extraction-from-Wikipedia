import matplotlib.pyplot as plt
import wiki_parser
import wiki_trivia_metric_calculator
import os
import textwrap
import algorithm_wrapper

category_entity_cache_dir = "catentcache/"
output_cache_graph = "graphCache/"

def drawSimPlot(entity, category):
    wiki_parser_instance = wiki_parser.WikiParser()
    wiki_trivia_metric_calculator_instance = wiki_trivia_metric_calculator.WikiTriviaMetricCalculator()
    tokens = wiki_parser_instance.getEntityTokens(entity)
    topk1 = wiki_trivia_metric_calculator_instance.getTopKTFIDFforEntity(tokens)
    full_path = category_entity_cache_dir + category + '/'
    outer_list = []
    for (root, dirs, files) in os.walk(full_path):
        for file in files:
            if file.endswith('.txt'):
                inner_list = []
                current_file = open(os.path.join(root, file), "r")
                for line in current_file:
                    line = line.replace('\n', '')
                    inner_list.append(line)
                outer_list.append(inner_list)
    size_new = len(outer_list)
    sim_list = []
    for i in range(0, size_new):
        sim_list.append(wiki_trivia_metric_calculator_instance.getEntitySimilarity(topk1, outer_list[i]))
    tups = zip(*enumerate(sim_list))
    plt.plot(tups[0], tups[1], label=str("10"), color="r")
    plt.ylim((0.0, 1.0))
    plt.legend().draggable()
    plt.show()

def drawSimPlotFixed(wiki_parser_instance, wiki_trivia_metric_calculator_instance):
    initial_list = ["Jimmy Carter", "Bill Clinton", "Hillary Clinton", "Elizabeth Warren", "Joe Biden", "Chuck Schumer"]
    grammy_winners = ["Paula Abdul", "50 Cent", "Adele", "Yolanda Adams", "Bryan Adams", "John Addison"]
    tokens = wiki_parser_instance.getEntityTokens("Barack Obama")
    topk_contenders = [5, 10, 20, 40, 50]
    colors = ["r", "g", "b", "y", "m"]
    plt.figure(2)
    size_new = len(topk_contenders)
    for i in range(0, size_new):
        wiki_trivia_metric_calculator_instance.k_val = topk_contenders[i]
        topk1 = wiki_trivia_metric_calculator_instance.getTopKTFIDFforEntity(tokens)
        graph_list = []
        for val in initial_list:
            top_current = wiki_parser_instance.getEntityTokens(val)
            topk_current = wiki_trivia_metric_calculator_instance.getTopKTFIDFforEntity(top_current)
            graph_list.append(wiki_trivia_metric_calculator_instance.getEntitySimilarity(topk1, topk_current))
        tups = zip(*enumerate(graph_list))
        plt.subplot(211)
        plt.xticks(tups[0], [textwrap.fill(text, 10) for text in initial_list])
        plt.ylim((0.0, 1.0))
        plt.plot(tups[0], tups[1], label=str(topk_contenders[i]), color=colors[i])

        graph_list_new = []
        for val in grammy_winners:
            top_current = wiki_parser_instance.getEntityTokens(val)
            topk_current = wiki_trivia_metric_calculator_instance.getTopKTFIDFforEntity(top_current)
            graph_list_new.append(wiki_trivia_metric_calculator_instance.getEntitySimilarity(topk1, topk_current))
        tups_new = zip(*enumerate(graph_list_new))
        plt.subplot(212)
        plt.xticks(tups_new[0], [textwrap.fill(text, 10) for text in grammy_winners])
        plt.ylim((0.0, 1.0))
        plt.plot(tups_new[0], tups_new[1], label=str(topk_contenders[i]), color=colors[i])
    plt.legend(title="Top k tokens").draggable()
    plt.show()


def drawScatterPlot(entity):
    x = []
    y = []
    anno = []
    cats = ["Category20thcenturyAmericanwriters", "CategoryAmericanNobellaureates", "CategoryGrammyAwardwinners"
            , "CategoryWashingtonDCDemocrats", "CategoryPunahouSchoolalumni", "Category1961births", "CategoryUnitedStatespresidentialcandidates2012",
            "CategoryPoliticiansfromChicago"]
    path = output_cache_graph
    max_count = 10
    for (root, dirs, files) in os.walk(path):
        count = 0
        for file in files:
            if file.endswith('.txt'):
                current_file = open(os.path.join(root, file), "r")
                odd = True
                anno.append(file[:-4])
                for line in current_file:
                    line = line.replace('\n', '')
                    if odd:
                        x.append(line)
                    else:
                        y.append(line)
                    odd = False
    plt.figure(3)
    fig, ax = plt.subplots()
    plt.title("Barack Obama Cohesiveness vs Surprise")
    plt.xlabel("Surprise")
    plt.ylabel("Cohesiveness")
    ax.scatter(x, y)
    for i, txt in enumerate(anno):
        if txt in cats:
            ax.annotate(txt, (x[i], y[i]))
    print(len(anno))
    plt.show()

def graphCache(entity, wiki_parser_instance, wiki_trivia_metric_calculator_instance):
    entity_cats = wiki_parser_instance.getCategoryForEntity(entity)
    if not os.path.exists(output_cache_graph):
        os.makedirs(output_cache_graph)
    for entity_cat in entity_cats:
        full_path = output_cache_graph + algorithm_wrapper.cleanifyPath(entity_cat) + ".txt"
        surprise = algorithm_wrapper.surprise(entity, entity_cat, wiki_parser_instance,wiki_trivia_metric_calculator_instance)
        if surprise:
            cohes = algorithm_wrapper.cohesivness(entity_cat.split(":")[1], wiki_trivia_metric_calculator_instance)
            if cohes:
                target = open(full_path, "w")
                target.write('%s' % surprise)
                target.write("\n")
                target.write('%s' % cohes)
                target.write("\n")
                target.close()




