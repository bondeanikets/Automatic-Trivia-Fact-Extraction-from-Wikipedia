from flask import Flask
from flask import Flask, render_template, json, jsonify
from flask import Flask, request, send_from_directory
import os
import algorithm_wrapper
import random
from random import randint

app = Flask(__name__,static_folder='templates')
@app.route("/")
def main():
   	print(os.getcwd())
   	return render_template('index.html')

@app.route("/entity", methods=['POST'])
def entity():
    _entity = request.form['searchfield']
    data = algorithm_wrapper.triviaAlgorithm(_entity)
    data = [element[0] for element in data]
    return render_template('entity.html',data = json.dumps(data),entity =_entity)

@app.route("/questions")
def questions():
    dir_path = "outputCache/"
    output_dict = {}
    questions_array = []
    max_count = 5
    entities = []
    for (root, dirs, files) in os.walk(dir_path):
        for file in files:
            if len(questions_array) > 100:
                break
            if file.endswith('.txt'):
                current_file = open(os.path.join(root, file), "r")
                count = 0
                for line in current_file:
                    inner_dict = {}
                    question = file[:-4] + " is a member of "
                    entities.append(file[:-4])
                    line = line.split(":")[0]
                    random_number = randint(0,9)
                    if random_number < 4:
                        question = file[:-4] + " is not a member of "
                        random_number_new = randint(0,8)
                        if random_number_new < 6 and len(entities) > 6:
                           while True:
                               rand_size = randint(0, len(entities)-1)
                               if entities[rand_size] != file[:-4]:
                                   question = entities[rand_size] + " is a member of "
                                   break
                        else:
                            question = file[:-4] + " is not a member of "
                        question += line.replace('\n', '')
                        inner_dict["question"] = question
                        inner_dict["correct_answer"] = "False"
                        inner_dict["incorrect_answers"] = ["True"]
                    else:
                        question += line.replace('\n', '')
                        inner_dict["question"] = question
                        inner_dict["correct_answer"] = "True"
                        inner_dict["incorrect_answers"] = ["False"]
                    questions_array.append(inner_dict)
                    if count > max_count:
                        break
                    count += 1
    print(questions_array)
    output_dict["results"] = [questions_array[i] for i in sorted(random.sample(xrange(len(questions_array)), 5)) ]
    print(output_dict)
    return jsonify(output_dict)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('templates/js', path)

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('templates', path)

if __name__ == "__main__":
    app.run()
