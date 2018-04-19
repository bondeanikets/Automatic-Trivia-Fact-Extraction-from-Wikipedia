import algorithm_wrapper
import wikipedia as wiki
import pdb
import wiki_parser
import wiki_trivia_metric_calculator


if __name__ == "__main__":
    wiki_parser_instance = wiki_parser.WikiParser()
    wiki_trivia_metric_calculator_instance = wiki_trivia_metric_calculator.WikiTriviaMetricCalculator()
    print("Init done")
    target = open("input.txt", "r")
    for line in target:
        line = line.replace('\n', '')
        print(algorithm_wrapper.triviaAlgorithm(line, wiki_parser_instance, wiki_trivia_metric_calculator_instance))
    target.close()