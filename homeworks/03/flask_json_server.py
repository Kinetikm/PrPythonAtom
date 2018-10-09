from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get_classifier_result/<version>", methods=['GET', 'POST'])
def return_classifier_result(version):
    #TODO прочитать из полученного запроса json-контент
    #В случае, если version==1, то должен вернуться json с версией и полем predict из входящего jsonа
    #В случае, если version==0, то должен вернуться json с версией и полем old_predict из входящего jsonа

@app.route("/")
def hello():
    #TODO должна возвращатьс инструкция по работе с сервером
    return 

if __name__ == "__main__":
    app.run()
