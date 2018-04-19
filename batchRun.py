import algorithm_wrapper
import wiki_parser
import wiki_trivia_metric_calculator
import sys
import os

if __name__ == "__main__":
    file_path = "./topEntityList.txt"
    # Read the each line of the entityList and Run the Trivia Algorithm
    if os.path.isfile(file_path):
        open_entityFile = open(file_path, "r")
        wiki_parser_instance = wiki_parser.WikiParser()
        wiki_trivia_metric_calculator_instance = wiki_trivia_metric_calculator.WikiTriviaMetricCalculator()
        for entity in open_entityFile:
            algorithm_wrapper.triviaAlgorithm(entity,wiki_parser_instance,wiki_trivia_metric_calculator_instance)
        open_entityFile.close()