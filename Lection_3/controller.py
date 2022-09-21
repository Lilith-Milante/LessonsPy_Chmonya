import model_sub as model #связываем модули между собой (пишем нужный)
import view

def button_click():
    value_a = view.get_value() # обращаемся к методу, который прописан в модуле view
    value_b = view.get_value()
    model.init(value_a, value_b) # инициал данные, передава входные данные
    result = model.do_it()
    view.view_data(result, 'result')