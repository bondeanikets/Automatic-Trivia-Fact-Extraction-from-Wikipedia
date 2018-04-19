import graphplot
import wiki_parser
import wiki_trivia_metric_calculator
wiki_parser_instance = wiki_parser.WikiParser()
wiki_trivia_metric_calculator_instance = wiki_trivia_metric_calculator.WikiTriviaMetricCalculator()
graphplot.drawSimPlotFixed(wiki_parser_instance, wiki_trivia_metric_calculator_instance)
graphplot.drawScatterPlot("Barack Obama", wiki_parser_instance, wiki_trivia_metric_calculator_instance)
#graphplot.graphCache("Barack Obama", wiki_parser_instance, wiki_trivia_metric_calculator_instance)
#graphplot.drawScatterPlot("Barack Obama")
